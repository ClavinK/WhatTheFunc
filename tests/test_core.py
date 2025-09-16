from whatthefunc import core
from dotenv import load_dotenv
import os

load_dotenv(override=True)

key = os.getenv("OPENAI_API_KEY")
new = core.WTF(key)

def test_wtfunc():
    assert new.wtfunc("pd.DataFrame()")
    