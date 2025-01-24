from fastapi import APIRouter, Request
from models.translator import translate_text

router = APIRouter()

@router.post("/translate")
async def translate(request: Request):
    form_data = await request.form()
    text = form_data["text"]
    target_lang = form_data["target_lang"]
    
    # 调用翻译模型
    translated_text = translate_text(text, target_lang)
    
    return {"translated_text": translated_text} 