from gradio_client import Client, handle_file
from os import getenv
from dotenv import load_dotenv
from playsound3 import playsound

load_dotenv()

print(getenv("REF_WAV_PATH"))
client = Client("http://localhost:9872/")

def ai_tts(prompt = "你媽是不是躺贏狗"):
	result = client.predict(
			ref_wav_path=handle_file(getenv("REF_WAV_PATH")),
			prompt_text="阿然後完了月底一解算，哎呀，我老爸得了MVP！",
			prompt_language="中英混合",
			text=prompt+"!",
			text_language="中英混合",
			how_to_cut="凑四句一切",
			top_k=23,
			top_p=1,
			temperature=1,
			ref_free=False,
			speed=0.85,
			if_freeze=False,
			inp_refs=None,
			sample_steps="32",
			if_sr=False,
			pause_second=0.28,
			api_name="/get_tts_wav"
	)
	print(f"result_path: {result}")
	playsound(result)