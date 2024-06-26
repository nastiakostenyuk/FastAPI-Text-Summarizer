from settings import app
from utils.models import TextToSummarize
from utils.diff_func import summarize_text


@app.post("/summarize")
async def summarize(text_to_summarize: TextToSummarize):
    """ Endpoint that summarizes text from a post request """
    result = await summarize_text(text_to_summarize.text)
    return {"summarized_text": result}

