#!/bin/bash

MODEL_PATH="/YOUR_MODEL_PATH/StarCore-9B/"
HOST="0.0.0.0"
LOG_LEVEL="warning"

# 定义要使用的GPU ID和对应的端口
declare -A GPU_MAP
GPU_MAP[0]=30000
# 多GPU部署
#GPU_MAP[1]=30001
#GPU_MAP[2]=30002
#GPU_MAP[3]=30003
#GPU_MAP[4]=30004
#GPU_MAP[5]=30005
#GPU_MAP[6]=30006
#GPU_MAP[7]=30007

echo "正在启动多GPU SGLang服务..."

for gpu_id in "${!GPU_MAP[@]}"; do
    port=${GPU_MAP[$gpu_id]}
    echo "在 GPU $gpu_id 上启动服务，端口: $port"
    CUDA_VISIBLE_DEVICES=$gpu_id python3 -m sglang.launch_server \
        --model-path $MODEL_PATH \
        --host $HOST \
        --port $port \
	      --mem-fraction-static 0.9 \
	      --trust-remote-code \
        --log-level $LOG_LEVEL &
    sleep 5 # 等待几秒，避免端口冲突和日志混杂
done

echo "所有服务启动命令已发送。使用 'ps aux | grep sglang' 查看进程。"
echo "服务地址:"
for gpu_id in "${!GPU_MAP[@]}"; do
    echo "  GPU $gpu_id -> http://${HOST}:${GPU_MAP[$gpu_id]}"
done