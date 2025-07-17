

import gradio as gr

# Arabic and English alphabets
arabic_alphabet = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
english_alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
english_alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def detect_language(text):
    for char in text:
        if char in arabic_alphabet:
            return "arabic"
        elif char in english_alphabet_lower + english_alphabet_upper:
            return "english"
    return "unknown"

def caesar_encrypt(text, shift, lang):
    result = ""
    
    if lang == "arabic":
        for char in text:
            if char in arabic_alphabet:
                index = arabic_alphabet.index(char)
                shifted_index = (index + shift) % len(arabic_alphabet)
                result += arabic_alphabet[shifted_index]
            else:
                result += char
    elif lang == "english":
        for char in text:
            if char in english_alphabet_lower:
                index = english_alphabet_lower.index(char)
                shifted_index = (index + shift) % 26
                result += english_alphabet_lower[shifted_index]
            elif char in english_alphabet_upper:
                index = english_alphabet_upper.index(char)
                shifted_index = (index + shift) % 26
                result += english_alphabet_upper[shifted_index]
            else:
                result += char
    else:
        result = "Unsupported language"
    
    return result

def caesar_decrypt(text, shift, lang):
    return caesar_encrypt(text, -shift, lang)

def run_cipher(text, shift, mode):
    lang = detect_language(text)
    if lang == "unknown":
        return "❌ Unsupported or unrecognized language."
    
    if mode == "Encrypt":
        return caesar_encrypt(text, shift, lang)
    else:
        return caesar_decrypt(text, shift, lang)

# Gradio Interface
with gr.Blocks(title="Caesar Cipher (Arabic & English)") as app:
    gr.Markdown("## 🔐 Caesar Cipher - Supports Arabic & English")

    with gr.Row():
        text_input = gr.Textbox(label="✏️ Enter your text")
        shift_input = gr.Slider(1, 25, value=3, step=1, label="🔁 Shift Value")

    mode_choice = gr.Radio(choices=["Encrypt", "Decrypt"], value="Encrypt", label="Mode")

    run_button = gr.Button("🔄 Run Caesar Cipher")
    result_output = gr.Textbox(label="✅ Result")

    run_button.click(fn=run_cipher, inputs=[text_input, shift_input, mode_choice], outputs=result_output)

app.launch()