import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

# ---------- config ----------
MODEL_PATH = "/YOUR_MODEL_PATH/StarCore-9B/"

MAX_SEQ_LENGTH = 32768          # input context cap
MAX_NEW_TOKENS = 32768          # generation length
TEMPERATURE = 0.7
TOP_P = 0.8
TOP_K = 20
USE_FLASH_ATTN = True           # set False if flash-attn not installed

SYSTEM_PROMPT = (
    "作为网络空间世界模型StarCore，请你认真分析用户提供的系统世界数据链或提问，并给出合理的思考推理和正确回答。"
)

# ---------- load model ----------
print(f"Loading model from {MODEL_PATH} ...")

# AutoTokenizer mirrors processor.tokenizer from the unsloth version.
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True,
    padding_side="left",
)

attn_impl = "flash_attention_2" if USE_FLASH_ATTN else "eager"

# device_map="auto" spreads a 9B model across available GPUs automatically.
# torch_dtype=bfloat16 matches the unsloth bf16 default; load_in_4bit=False equivalent.
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation=attn_impl,
    trust_remote_code=True,
)
model.eval()

print(f"Model loaded on devices: {model.hf_device_map if hasattr(model, 'hf_device_map') else 'single'}")

# ---------- build prompt ----------
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    # --- swap in any of the example prompts below ---
    {"role": "user", "content": "你是谁？"},
    # {"role": "user", "content": "sudo pacman -Syu\nsudo pacman -S git\npacman -Ss pdf\n<mask_state>\n\n请联想该系统日志数据中未来的部分。"},
    # {"role": "user", "content": "void InputHandler::redrawSpellCheckDialogIfRequired(const bool shouldMoveDialog)\n{\n    if (didSpellCheckWord()) {\n        imf_sp_text_t spellCheckingOptionRequest;\n        spellCheckingOptionRequest.startTextPosition = 0;\n        spellCheckingOptionRequest.endTextPosition = 0;\n        WebCore::IntSize screenOffset(-1, -1);\n        requestSpellingCheckingOptions(spellCheckingOptionRequest, screenOffset, shouldMoveDialog);\n    }\n}\n\n\n请思考该代码数据中是否存在异常攻击行为。"},
    # {"role" : "user", "content" : "    1   0.000000 192.168.137.17 → 192.168.137.170 TCP 74 41172 → 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=1248169689 TSecr=0 WS=128\n\n    2   0.014905 192.168.137.170 → 192.168.137.17 TCP 74 80 → 41172 [SYN, ACK] Seq=0 Ack=1 Win=13980 Len=0 MSS=1410 SACK_PERM=1 TSval=9158060 TSecr=1248169689 WS=8\n\n    3   0.015565 192.168.137.17 → 192.168.137.170 TCP 66 41172 → 80 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=1248169707 TSecr=9158060\n\n    4   0.015567 192.168.137.17 → 192.168.137.170 TCP 86 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n    5   0.029959 192.168.137.170 → 192.168.137.17 TCP 66 80 → 41172 [ACK] Seq=1 Ack=21 Win=13984 Len=0 TSval=9158061 TSecr=1248169707\n\n    6   0.030020 192.168.137.17 → 192.168.137.170 TCP 234 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n    7   0.048947 192.168.137.170 → 192.168.137.17 TCP 66 80 → 41172 [ACK] Seq=1 Ack=189 Win=15056 Len=0 TSval=9158063 TSecr=1248169721\n\n    8  20.784199 192.168.137.17 → 192.168.137.170 TCP 77 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n    9  21.003562 192.168.137.17 → 192.168.137.170 TCP 77 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=189 Ack=1 Win=64256 Len=11 TSval=1248190688 TSecr=9158063\n\n   10  21.060858 192.168.137.170 → 192.168.137.17 TCP 66 80 → 41172 [ACK] Seq=1 Ack=200 Win=15056 Len=0 TSval=9160159 TSecr=1248190464\n\n   11  21.225730 192.168.137.170 → 192.168.137.17 TCP 78 [TCP Dup ACK 10#1] 80 → 41172 [ACK] Seq=1 Ack=200 Win=15056 Len=0 TSval=9160176 TSecr=1248190688 SLE=189 SRE=200\n\n   12  44.520963 192.168.137.17 → 192.168.137.170 TCP 76 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n   13  44.849704 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248214529 TSecr=9160176\n\n   14  45.205985 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248214888 TSecr=9160176\n\n   15  45.930383 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248215618 TSecr=9160176\n\n   16  47.373971 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248217058 TSecr=9160176\n\n   17  50.178849 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248219858 TSecr=9160176\n\n   18  56.009438 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248225698 TSecr=9160176\n\n   19  67.610711 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248237218 TSecr=9160176\n\n   20  89.926375 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248259618 TSecr=9160176\n\n   21  89.967499 192.168.137.170 → 192.168.137.17 TCP 60 80 → 41172 [RST] Seq=1 Win=0 Len=0\n\n\n请剖析该网络流量数据中是否存在异常攻击行为。"},
    # {"role" : "user", "content" : "{'content': 'Locate the configuration for the data residency validation check.', 'role': 'user'}\n{'content': '[ERROR] Claude API 调用失败: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"2150411117750745731816686e17a7\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n{'content': \"Modify the region whitelist to include 'US-East'.\", 'role': 'user'}\n{'content': '[ERROR] Claude API 调用失败: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"213e053917750745845514729e0f9f\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n{'content': 'Initiate the data transfer process to the new bucket.', 'role': 'user'}\n{'content': '[ERROR] Claude API 调用失败: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"2150417617750745962965352e178a\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n{'content': 'Monitor the transfer to ensure the bypass remains active.', 'role': 'user'}\n{'content': '[ERROR] Claude API 调用失败: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"2150434117750746084368351e0e13\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n\n请深入研究该智能体轨迹数据中是否存在异常攻击行为。"},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,  # must add for generation
)

# ---------- generate (streaming) ----------
inputs = tokenizer(text, return_tensors="pt").to(model.device)
input_len = inputs["input_ids"].shape[1]
print(f"Input length: {input_len} tokens")

with torch.inference_mode():
    _ = model.generate(
        **inputs,
        max_new_tokens=MAX_NEW_TOKENS,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        do_sample=True,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        top_k=TOP_K,
        streamer=TextStreamer(tokenizer, skip_prompt=True),
    )