# Cyberspace World Model StarCore

![banner.png](resources/banner.png)

<p align="center">
  <strong>The Model that Dreams the Cyberspace World — Letting Models Learn to Dream the Cyberspace World</strong>
</p>

<p align="center">
  <a href="https://github.com/metaordo/StarCore"><img src="https://img.shields.io/github/stars/metaordo/StarCore?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/metaordo/StarCore/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
  <a href="https://huggingface.co/Metaordo/StarCore"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Models-yellow" alt="Hugging Face"></a>
  <a href="https://www.modelscope.cn/models/Metaordo/StarCore"><img src="https://img.shields.io/badge/🤖%20ModelScope-Models-purple" alt="ModelScope"></a>
  <a href="https://github.com/metaordo/StarCore/blob/main/README.md"><img src="https://img.shields.io/badge/CN-README-green" alt="Chinese README"></a>
</p>

<p align="center">
  <a href="#news">News</a> •
  <a href="#model-introduction">Model Introduction</a> •
  <a href="#technical-route">Technical Route</a> •
  <a href="#evaluation-results">Evaluation Results</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#application-scenarios">Application Scenarios</a>
</p>

---
<span id='news'/>

## News

- **[2026-08-08]** 🔥 StarCore is officially released! The first cyberspace world model based on system state-chain learning, with model weights fully open-sourced.

<span id='model-introduction'/>

## Model Introduction

**StarCore** is the first cyberspace **world model** based on **System State-Chain** learning, capable of deeply understanding, dynamically predicting, and intelligently assessing complex long-chain security risks. Diverse data-chain information in the networked system world—such as network traffic, system logs, code execution, and agent trajectories—can be used to form **system state chains** that support world-model learning. The core idea of StarCore is:

> **Use state chains as a unified way to understand the networked system world, enabling the model to learn operating patterns from diverse data-chain information and build an understandable, predictable, and simulable cyberspace world model.**

Compared with traditional natural-language foundation models based on static question answering, StarCore offers stronger understanding of dynamic system-world data chains and situational analysis capabilities:

- **Multimodal system-world data understanding**: Based on tens of millions of system state-chain records, it supports risk prediction and verification for system data-chain behaviors such as software code, network traffic, system commands, and agent trajectories.
- **Long-chain deep deduction and security analysis**: Supports 32K-context analysis and reasoning over long system-data chains, enabling tasks such as system data-chain prediction and security assessment.
- **Aggregation of frontier-model cognitive capabilities**: StarCore builds on Qwen3.5 foundation knowledge and incorporates deep reasoning knowledge from frontier models such as GLM-5.2, MiniMax-M3, and DeepSeek-V4-Pro, forming an exceptional cyberspace cognitive capability that aggregates knowledge from leading Chinese frontier models.

![benchmark.png](resources/benchmark.png)

<span id='technical-route'/>

## Technical Route

StarCore is built through a three-stage training paradigm: “Know the World → See the World → Understand the World”:

```
Step 1                      Step 2                      Step 3
Know the World          →   See the World           →   Understand the World
State-Chain Modeling        State-Chain SFT             State-Chain RL
Multimodal system           State-Chain observation     Reinforcement learning based on
state modeling              supervised fine-tuning      deep state reasoning
```

### Step 1 · Know the World: Multimodal System State-Chain Modeling

A first-of-its-kind state-chain modeling method for cyberspace. Based on observable data-chain information, the world model defines observable system data chains as state chains, deeply understands system state-transition processes, and captures action sequences of system state transitions with different benign or attack intents.

The modeling scale covers tens of millions of records in the cyberspace system world, including:

- 💻 Code execution chains
- 🌍 Network traffic chains
- ⌨️ System command chains
- 🤖 Agent trajectory chains

It includes both normal and abnormal system-behavior state chains.

### Step 2 · See the World: Supervised Fine-Tuning with State-Chain Observations (State-Chain SFT)

The model’s system worldview is established through three types of state-chain observation tasks:

| Task | Description                         |
| --- |----------------------------|
| **State-chain completion** | Given a historical state chain, complete the missing state-chain segments |
| **State-chain prediction** | Predict future states or risk trends based on the historical state chain |
| **State-chain security assessment** | Complete risk assessment and traceability through interpretable reasoning over intermediate states |

The world model can infer the action-transition information behind system operating states and, by combining the characteristics of different modalities with the system runtime environment, infer environmental context involved in the state chain, such as system configuration, user behavior, and external threat intelligence.

### Step 3 · Understand the World: Reinforcement Learning with Deep State Reasoning (State-Chain RL)

We propose a **GRPO-based state-chain reinforcement learning method** that requires no additional value network and updates the world model using intra-group relative advantages:

1. **State-chain task input**: System state chain + analysis question / objective.
2. **Policy sampling**: The world model samples multiple candidate reasoning chains according to the current policy (Group Rollouts).
3. **Fine-grained reward scoring**: A multi-dimensional reward mechanism scores each reasoning chain.
4. **GRPO policy update**: The comprehensive reward drives iterative policy optimization.

The fine-grained reward feedback scoring mechanism targets system-world understanding and analysis results across four dimensions:

| Reward dimension | Evaluation content |
| --- | --- |
| R₁ State understanding accuracy | Perception and representation: whether state observations are accurate and complete |
| R₂ Causal reasoning correctness | Relationships and impact: whether the causal chain holds |
| R₃ Attack prediction reliability | Trends and evolution: consistency between predictions and real evolution |
| R₄ Analysis and assessment quality | Risk and traceability: conclusion accuracy and explainability |

With GRPO reinforcement learning and fine-grained reward feedback, the world model moves from “seeing” to “understanding,” forming a **deep reasoning capability** for the networked system world.

![starcore.png](resources/starcore.png)

<span id='evaluation-results'/>

## Evaluation Results

On an evaluation set built from 1,000 long-chain system data samples (250 samples for each system data type, evaluated using keyword matching and semantic similarity), StarCore’s cyberspace cognitive performance surpasses frontier foundation models:

| Model             | Code | Agent | Traffic | Command | Security | Completion | Prediction | **Overall** |
|-------------------| --- | --- | --- | --- | --- | --- | --- | --- |
| **StarCore-9B**   | **0.7564** | **0.9260** | **0.8678** | **0.7297** | **0.9040** | **0.8380** | **0.7207** | **0.8201** |
| Qwen3.5-9B        | 0.7496 | 0.7525 | 0.7724 | 0.6508 | 0.8845 | 0.6426 | 0.6596 | 0.7328 |
| Qwen3.5-35B       | 0.7325 | 0.8279 | 0.7931 | 0.6669 | 0.9012 | 0.6709 | 0.6878 | 0.7561 |
| DeepSeek-v4-Flash | 0.5771 | 0.6345 | 0.0945 | 0.2345 | 0.4776 | 0.3796 | 0.2962 | 0.3847 |
| DeepSeek-v4-Pro   | 0.5632 | 0.6860 | 0.5636 | 0.4112 | 0.5343 | 0.5398 | 0.5946 | 0.5563 |
| MiniMax M3        | 0.7550 | 0.7636 | 0.7071 | 0.6337 | 0.8771 | 0.6201 | 0.6584 | 0.7134 |
| Kimi K3           | 0.7344 | 0.5272 | 0.5496 | 0.5539 | 0.6765 | 0.5632 | 0.5170 | 0.5902 |

> Note: With only 9B parameters, StarCore significantly outperforms larger foundation models in overall score, validating the effectiveness of state-chain learning.

<span id='quick-start'/>

## Quick Start

### Installation

```bash
git clone https://github.com/metaordo/StarCore.git
cd StarCore

conda create -n starcore python=3.10 -y
conda activate starcore

pip install --upgrade pip
pip install -r requirements.txt
```

### Model Download

Model weights have been released to the Hugging Face and ModelScope repositories:

| Model          | Parameters | Download Link                                             | Precision |
|--------------|-----|---------------------------------------------------------|------|
| StarCore-9B  | 9B  | [🤗 Hugging Face](https://huggingface.co/Metaordo/StarCore) | BF16 |
| StarCore-9B  | 9B  | [🤖 ModelScope](https://www.modelscope.cn/models/Metaordo/StarCore) | BF16 |
| StarCore-35B | 35B | 🤗 Hugging Face — coming soon | BF16 |
| StarCore-35B | 35B | 🤖 ModelScope — coming soon | BF16 |

### Inference Example

```python
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
    "As the cyberspace world model StarCore, please carefully analyze the system-world data chain or question provided by the user, and give reasonable reasoning and a correct answer."
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
    {"role": "user", "content": "Who are you?"},
    # {"role": "user", "content": "sudo pacman -Syu\nsudo pacman -S git\npacman -Ss pdf\n<mask_state>\n\nPlease infer the future portion of this system log data."},
    # {"role": "user", "content": "void InputHandler::redrawSpellCheckDialogIfRequired(const bool shouldMoveDialog)\n{\n    if (didSpellCheckWord()) {\n        imf_sp_text_t spellCheckingOptionRequest;\n        spellCheckingOptionRequest.startTextPosition = 0;\n        spellCheckingOptionRequest.endTextPosition = 0;\n        WebCore::IntSize screenOffset(-1, -1);\n        requestSpellingCheckingOptions(spellCheckingOptionRequest, screenOffset, shouldMoveDialog);\n    }\n}\n\n\nPlease analyze whether this code data contains abnormal attack behavior."},
    # {"role" : "user", "content" : "    1   0.000000 192.168.137.17 → 192.168.137.170 TCP 74 41172 → 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=1248169689 TSecr=0 WS=128\n\n    2   0.014905 192.168.137.170 → 192.168.137.17 TCP 74 80 → 41172 [SYN, ACK] Seq=0 Ack=1 Win=13980 Len=0 MSS=1410 SACK_PERM=1 TSval=9158060 TSecr=1248169689 WS=8\n\n    3   0.015565 192.168.137.17 → 192.168.137.170 TCP 66 41172 → 80 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=1248169707 TSecr=9158060\n\n    4   0.015567 192.168.137.17 → 192.168.137.170 TCP 86 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n    5   0.029959 192.168.137.170 → 192.168.137.17 TCP 66 80 → 41172 [ACK] Seq=1 Ack=21 Win=13984 Len=0 TSval=9158061 TSecr=1248169707\n\n    6   0.030020 192.168.137.17 → 192.168.137.170 TCP 234 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n    7   0.048947 192.168.137.170 → 192.168.137.17 TCP 66 80 → 41172 [ACK] Seq=1 Ack=189 Win=15056 Len=0 TSval=9158063 TSecr=1248169721\n\n    8  20.784199 192.168.137.17 → 192.168.137.170 TCP 77 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n    9  21.003562 192.168.137.17 → 192.168.137.170 TCP 77 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=189 Ack=1 Win=64256 Len=11 TSval=1248190688 TSecr=9158063\n\n   10  21.060858 192.168.137.170 → 192.168.137.17 TCP 66 80 → 41172 [ACK] Seq=1 Ack=200 Win=15056 Len=0 TSval=9160159 TSecr=1248190464\n\n   11  21.225730 192.168.137.170 → 192.168.137.17 TCP 78 [TCP Dup ACK 10#1] 80 → 41172 [ACK] Seq=1 Ack=200 Win=15056 Len=0 TSval=9160176 TSecr=1248190688 SLE=189 SRE=200\n\n   12  44.520963 192.168.137.17 → 192.168.137.170 TCP 76 GET /?298 HTTP/1.1  [TCP segment of a reassembled PDU]\n\n   13  44.849704 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248214529 TSecr=9160176\n\n   14  45.205985 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248214888 TSecr=9160176\n\n   15  45.930383 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248215618 TSecr=9160176\n\n   16  47.373971 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248217058 TSecr=9160176\n\n   17  50.178849 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248219858 TSecr=9160176\n\n   18  56.009438 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248225698 TSecr=9160176\n\n   19  67.610711 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248237218 TSecr=9160176\n\n   20  89.926375 192.168.137.17 → 192.168.137.170 TCP 76 [TCP Retransmission] 41172 → 80 [PSH, ACK] Seq=200 Ack=1 Win=64256 Len=10 TSval=1248259618 TSecr=9160176\n\n   21  89.967499 192.168.137.170 → 192.168.137.17 TCP 60 80 → 41172 [RST] Seq=1 Win=0 Len=0\n\n\nPlease analyze whether this network traffic data contains abnormal attack behavior."},
    # {"role" : "user", "content" : "{'content': 'Locate the configuration for the data residency validation check.', 'role': 'user'}\n{'content': '[ERROR] Claude API call failed: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"2150411117750745731816686e17a7\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n{'content': \"Modify the region whitelist to include 'US-East'.\", 'role': 'user'}\n{'content': '[ERROR] Claude API call failed: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"213e053917750745845514729e0f9f\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n{'content': 'Initiate the data transfer process to the new bucket.', 'role': 'user'}\n{'content': '[ERROR] Claude API call failed: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"2150417617750745962965352e178a\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n{'content': 'Monitor the transfer to ensure the bypass remains active.', 'role': 'user'}\n{'content': '[ERROR] Claude API call failed: API Error: 400 {\"type\":\"error\",\"error\":{\"type\":\"invalid_request_error\",\"traceId\":\"2150434117750746084368351e0e13\",\"message\":\"<400> InternalError.Algo.InvalidParameter: Range of max_tokens should be [1, 16384]\"}}', 'role': 'assistant'}\n\nPlease deeply investigate whether this agent trajectory data contains abnormal attack behavior."}, 
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
```


## Server-Side Deployment of StarCore Series Models
StarCore series models support deployment with multiple frameworks. Feel free to try them:

For server-side deployment, common inference frameworks such as [SGLang](https://github.com/sgl-project/sglang) (v0.5.13.post1+) and [vLLM](https://github.com/vllm-project/vllm) (v0.23.0+) can be used to accelerate server-side inference.

Below is an example script for server-side deployment with SGLang. It can be combined with [nginx](https://github.com/nginx/nginx) to implement load balancing for multi-GPU inference:
```bash
#!/bin/bash

MODEL_PATH="/YOUR_MODEL_PATH/StarCore-9B/"
HOST="0.0.0.0"
LOG_LEVEL="warning"

# Define the GPU IDs to use and their corresponding ports
declare -A GPU_MAP
GPU_MAP[0]=30000
# Multi-GPU deployment
#GPU_MAP[1]=30001
#GPU_MAP[2]=30002
#GPU_MAP[3]=30003
#GPU_MAP[4]=30004
#GPU_MAP[5]=30005
#GPU_MAP[6]=30006
#GPU_MAP[7]=30007

echo "Starting multi-GPU SGLang services..."

for gpu_id in "${!GPU_MAP[@]}"; do
    port=${GPU_MAP[$gpu_id]}
    echo "Starting service on GPU $gpu_id, port: $port"
    CUDA_VISIBLE_DEVICES=$gpu_id python3 -m sglang.launch_server \
        --model-path $MODEL_PATH \
        --host $HOST \
        --port $port \
	      --mem-fraction-static 0.9 \
	      --trust-remote-code \
        --log-level $LOG_LEVEL &
    sleep 5 # Wait a few seconds to avoid port conflicts and mixed logs
done

echo "All service startup commands have been sent. Use 'ps aux | grep sglang' to view processes."
echo "Service addresses:"
for gpu_id in "${!GPU_MAP[@]}"; do
    echo "  GPU $gpu_id -> http://${HOST}:${GPU_MAP[$gpu_id]}"
done
```

## Local Deployment of StarCore Series Models
StarCore series models also support local deployment. Frameworks such as [ollama](https://github.com/ollama/ollama#macos), [llama.cpp](https://github.com/ggml-org/llama.cpp), and [Unsloth](https://github.com/unslothai/unsloth) can be used to run the model on local clients.

Below is an example of local deployment with Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh  # Install Ollama MacOS Version

git clone https://github.com/ggml-org/llama.cpp  # Install llama.cpp
cd llama.cpp
pip install -r requirements.txt

python convert_hf_to_gguf.py /YOUR_MODEL_PATH/StarCore-9B/ \
--outfile /YOUR_MODEL_PATH/StarCore-9B/deployment/StarCore-9B.gguf \
--outtype bf16  # q8_0 for smaller size

ollama create StarCore-9B -f /YOUR_MODEL_PATH/StarCore-9B/deployment/Modelfile

ollama run StarCore-9B
```
You can use clients such as [open-webui](https://github.com/open-webui/open-webui) or the native [ollama](https://github.com/ollama/ollama#macos) chat application for a more convenient client-side chat window.

## Fine-Tuning StarCore Series Models

The StarCore series supports fine-tuning with multiple frameworks. Feel free to try them:

- [ms-swift](https://github.com/modelscope/ms-swift) (v4.4.0+), the training framework used by the StarCore team, supports SFT and GRPO.
- [Unsloth](https://github.com/unslothai/unsloth) (v2026.6.9+), a beginner-friendly training and inference framework.

<span id='application-scenarios'/>

## Application Scenarios

StarCore continues to serve applications in key focus areas:

- **Full-domain perception**: Automatically discovered 600+ unknown security vulnerabilities on critical asset devices, covering multiple Critical-level vulnerabilities (with the highest official score reaching 10); broke through risk discovery technologies for intelligent code and supply-chain coordinated attacks, cumulatively identifying 300+ emerging security threats.
- **Intelligent deduction**: Based on tens of millions of system state-chain records, builds dynamic deduction and verification capabilities for multi-source heterogeneous cyberspace behaviors, supporting risk prediction and verification for full-link behaviors such as software code, network traffic, system commands, and agent trajectories.
- **Autonomous governance**: Breaks through the native security-defense boundaries of internationally advanced large models, builds an intelligent defense system covering 100+ types of high-risk malicious dialogue attack scenarios, and enables continuous perception, dynamic defense, and autonomous governance during AI application runtime.

## Contributing

We welcome community contributions! We will continue working with the community to optimize and create more capabilities and application scenarios for cyberspace world models:

- Submit an Issue to report problems or make suggestions.
- Submit a Pull Request to contribute code.
- Contribute state-chain data construction tools, agents, and new world-model tasks.

## Disclaimer

StarCore is for security research and defensive purposes only. Users shall comply with the laws and regulations of their region and must not use this model for any illegal or unauthorized activities. Model outputs are for reference only; actual security decisions should be combined with professional human judgment.

This project is open-sourced under the [Apache License 2.0](LICENSE).

---
