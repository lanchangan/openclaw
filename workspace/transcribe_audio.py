# 使用Whisper将音频转为文字
import whisper
import os
import time

audio_path = r"C:\Users\LWS\.openclaw\workspace\bili_download\audio.mp3"
output_dir = r"C:\Users\LWS\.openclaw\workspace\bili_download"

print("=" * 60)
print("🎯 开始语音识别")
print("=" * 60)
print(f"音频文件: {audio_path}")
print(f"文件大小: {os.path.getsize(audio_path) / (1024*1024):.2f} MB")
print()

# 加载模型
print("📦 加载Whisper模型 (base)...")
print("   模型越大越准确，但速度越慢")
print("   base模型适合中文，速度与准确率平衡")
start_time = time.time()
model = whisper.load_model("base")
load_time = time.time() - start_time
print(f"✓ 模型加载完成，耗时: {load_time:.1f} 秒")
print()

# 开始转录
print("🎙️ 开始转录音频...")
print("   这可能需要一些时间，取决于音频长度")
print("   36分钟的音频预计需要 3-10 分钟")
print()
start_time = time.time()

result = model.transcribe(
    audio_path,
    language="zh",  # 指定中文
    task="transcribe",
    verbose=True,   # 显示进度
    fp16=False    # CPU运行用FP32
)

transcribe_time = time.time() - start_time
print()
print(f"✓ 转录完成！耗时: {transcribe_time:.1f} 秒")
print()

# 保存结果
print("💾 保存结果...")

# 1. 保存完整JSON
import json
json_path = os.path.join(output_dir, "transcription.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"   JSON: {json_path}")

# 2. 保存纯文本（逐字稿）
text_path = os.path.join(output_dir, "transcription.txt")
with open(text_path, "w", encoding="utf-8") as f:
    f.write(result["text"])
print(f"   文本: {text_path}")

# 3. 保存带时间戳的逐字稿
segments_path = os.path.join(output_dir, "transcription_with_timestamps.txt")
with open(segments_path, "w", encoding="utf-8") as f:
    f.write("=" * 60 + "\n")
    f.write("📝 逐字稿（带时间戳）\n")
    f.write("=" * 60 + "\n\n")
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()
        # 格式化时间 mm:ss
        start_str = f"{int(start//60):02d}:{int(start%60):02d}"
        end_str = f"{int(end//60):02d}:{int(end%60):02d}"
        f.write(f"[{start_str} - {end_str}] {text}\n\n")

print(f"   时间戳: {segments_path}")

# 4. 生成Word文档（简单格式）
doc_path = os.path.join(output_dir, "逐字稿.doc")
with open(doc_path, "w", encoding="utf-8") as f:
    f.write("=" * 60 + "\n")
    f.write("逐字稿\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"视频标题: 四年级下册《看看我们的地球》导读课-王秀萍\n")
    f.write(f"视频链接: https://www.bilibili.com/video/BV1u61mBhEj7/\n")
    f.write(f"转录时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"音频时长: {result.get('duration', 'N/A')} 秒\n\n")
    f.write("=" * 60 + "\n")
    f.write("正文\n")
    f.write("=" * 60 + "\n\n")
    f.write(result["text"])

print(f"   Word格式: {doc_path}")

print()
print("=" * 60)
print("✅ 全部完成！")
print("=" * 60)
print(f"\n📊 统计信息:")
print(f"   音频时长: {result.get('duration', 'N/A')} 秒 ({result.get('duration', 0)/60:.1f} 分钟)")
print(f"   转录文字数: {len(result['text'])} 字符")
print(f"   段落数: {len(result['segments'])}")
print(f"\n📁 输出文件:")
print(f"   1. {text_path}")
print(f"   2. {segments_path}")
print(f"   3. {doc_path}")
print(f"   4. {json_path}")
