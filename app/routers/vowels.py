# testing router (by @TomyRD)

""""Endpoint definitions"""
from fastapi import APIRouter
import re

router = APIRouter()


@router.get("/greeting/{name}")
async def greetings(name: str):
    """Greets you"""
    return f"Hola {name}! Te quiero mucho <3"


@router.get("/no_vowels/{word}")
async def no_vowels(word: str):
    """Removes vowels"""
    return re.sub("[aeiouAEIOU]", "", word)
