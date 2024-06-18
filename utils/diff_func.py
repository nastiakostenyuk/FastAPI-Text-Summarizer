from settings import summarizer


async def summarize_text(text: str) -> str:
    """ Summarizes the provided text using a transformers.pipline .

    Args:
        text (str): The text to be summarized.

    Returns:
        str: The summarized text.
    """
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
