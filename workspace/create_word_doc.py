# -*- coding: utf-8 -*-
"""Create Word document from transcription"""
import os
from datetime import datetime

def create_word_doc():
    # Read the transcription file
    txt_file = "逐字稿-看看我们的地球导读课.txt"
    
    if not os.path.exists(txt_file):
        print(f"Error: {txt_file} not found")
        return
    
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create HTML content (can be opened in Word)
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
