# 这里可以替换成实际的大语言模型API调用
def translate_text(text: str, target_lang: str) -> str:
    # 示例：简单的翻译逻辑
    translations = {
        "en": {"你好": "Hello", "世界": "World"},
        "es": {"你好": "Hola", "世界": "Mundo"},
    }
    
    if target_lang in translations:
        return " ".join(translations[target_lang].get(word, word) for word in text.split())
    return text 