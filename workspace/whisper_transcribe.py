# -*- coding: utf-8 -*-
"""
使用Whisper对视频进行语音识别
"""
import os
import sys

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Check if whisper is installed
try:
    import whisper
    print("Whisper is installed, loading model...")
except ImportError:
    print("Installing whisper...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "-U", "openai-whisper"])
    import whisper

# Load model
print("Loading Whisper base model (Chinese optimized)...")
model = whisper.load_model("base")
print("Model loaded!")

# Find video files
video_files = []
for f in os.listdir('bili_download'):
    if f.endswith('.mp4'):
        video_files.append(os.path.join('bili_download', f))

video_files.sort()
print(f"\nFound {len(video_files)} video files")

# Process each video
all_transcriptions = []

for i, video_path in enumerate(video_files, 1):
    print(f"\n{'='*60}")
    print(f"Processing video {i}/{len(video_files)}")
    print(f"File: {os.path.basename(video_path)}")
    print(f"{'='*60}")
    
    try:
        # Transcribe
        print("Transcribing with Whisper...")
        result = model.transcribe(
            video_path,
            language="zh",
            verbose=True
        )
        
        all_transcriptions.append(result)
        
        # Save individual file result
        output_prefix = f"transcription_part{i}"
        
        # Save text
        with open(f"{output_prefix}.txt", 'w', encoding='utf-8') as f:
            f.write(result["text"])
        print(f"Saved: {output_prefix}.txt")
        
        # Save JSON
        import json
        with open(f"{output_prefix}.json", 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Saved: {output_prefix}.json")
        
        print(f"Duration: {result.get('duration', 0):.1f} seconds")
        print(f"Segments: {len(result.get('segments', []))}")
        
    except Exception as e:
        print(f"Error processing video: {e}")
        import traceback
        traceback.print_exc()

# Combine all transcriptions into final output
print(f"\n{'='*60}")
print("Creating final combined transcription...")
print(f"{'='*60}")

# Create final transcript file
with open("逐字稿-看看我们的地球导读课.txt", 'w', encoding='utf-8') as f:
    f.write("=" * 60 + "\n")
    f.write("逐字稿\n")
    f.write("=" * 60 + "\n\n")
    f.write("视频标题: 四年级下册《看看我们的地球》导读课-王秀萍\n")
    f.write("视频链接: https://www.bilibili.com/video/BV1u61mBhEj7/\n")
    f.write("转录方式: Whisper语音识别\n\n")
    f.write("=" * 60 + "\n")
    f.write("正文\n")
    f.write("=" * 60 + "\n\n")
    
    for i, result in enumerate(all_transcriptions, 1):
        f.write(f"\n--- 第{i}部分 ---\n\n")
        f.write(result["text"])

print("Created: 逐字稿-看看我们的地球导读课.txt")

# Create timestamped version
with open("逐字稿-看看我们的地球导读课-带时间戳.txt", 'w', encoding='utf-8') as f:
    f.write("=" * 60 + "\n")
    f.write("逐字稿（带时间戳）\n")
    f.write("=" * 60 + "\n\n")
    f.write("视频标题: 四年级下册《看看我们的地球》导读课-王秀萍\n\n")
    
    for i, result in enumerate(all_transcriptions, 1):
        f.write(f"\n--- 第{i}部分 ---\n\n")
        
        for segment in result.get("segments", []):
            start = segment["start"]
            text = segment["text"].strip()
            
            mins = int(start // 60)
            secs = int(start % 60)
            time_str = f"{mins:02d}:{secs:02d}"
            
            f.write(f"[{time_str}] {text}\n")

print("Created: 逐字稿-看看我们的地球导读课-带时间戳.txt")

print(f"\n{'='*60}")
print("All done!")
print(f"{'='*60}")
print("\nOutput files:")
print("  1. 逐字稿-看看我们的地球导读课.txt")
print("  2. 逐字稿-看看我们的地球导读课-带时间戳.txt")
