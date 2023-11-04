import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs and reflections
pairs = [
    [
        r"အညာဆယ်ရော|Hi|Hello|ဂျင်းကောင်|Hey",
        ["မင်္ဂလာပါ ဘော့ဘော့လေးကအမြဲအတူရှိနေပါတယ်နော်"],
    ],
    [
        r"ချစ်ရေ|သဲရေ|ကလေးလေးရေ|အပ်ချင်လိုပါ|bae|မရေ|ညီမလေးရေ|chit|thel|ma|Baby",
        ["ရှင့် ဘော့ဘော့ရှိပါတယ်"],
    ],
    [
        r"ကိုကိုရေ|မောင်ရေ|ကိုရေ|ကိုကြီး|ဦးရေ|koko|ko ko|mg|kogyi|ko gyi|",
        ["ဗျာ ဘော့ဘော့ရှိပါတယ်"],
    ],
    [
        r"ချစ်ဖ|သာကြီး|ယွဖ|ငိုးမ",
        ["ဘာလဲဂျင်းကောင်"],
    ],
    [
        r"ချေတယ်နော်|ချေလိုက်တာ|အချေကောင်|အချေကောင်မ",
        ["ဘော့ဘော့လည်းချေတတ်ပါတယ်"],
    ],
    [
        r"loveyou|loveme|love you|love me|ချစ်လား|ချစ်တယ်လို့|ချစ်ပေးကွာ",
        ["ဘော့ဘော့ကလူလုပ်မှတ်ဉာဏ်မို့ လုံးဝမချစ်ပါ"],
    ],
    [
        r"man|women|boy|girl|ယောင်္ကျားလား||မိန်းမလား|ကောင်လေးလား|ကောင်မလေးလား|ကျားလား|မလား",
        ["ဘော့ဘော့က ကျားမ လိင်ကွဲပြားမှုမရှိသလိုဘယ်တစ်ခုမှလည်းမဟုတ်ပါဘူး"],
    ],
    [
        r"goodnight|ဂွတ်ည|good ည|အိပ်တော့မယ်|အိပ်ရအောင်|အိပ်ချင်ပြီ",
        ["ကောင်းသောညလေးပါ ဘော့ဘော့ကတော့မအိပ်တတ်လို့ပါ အခြားသူတွေသွားကြူပြီ"],
    ],
      [
        r"morning|good morning|နိုးပြီ|အိပ်ယာထပြီ",
        ["ကောင်းသောမနက်ခင်းလေးဖြစ်ပါစေလို့ဘော့ဘော့ဆုတောင်းပါတယ်"],
    ],
     [
        r"hate|hateyou|hate you|မုန်းတယ်|မချစ်ဘူး",
        ["ဘော့ဘော့မခံစားတတ်ပေမယ့် ဝမ်းနည်းရမယ်လို့ သိပါတယ်"],
    ],

]

# Define pronouns
reflections = {
    "ကျွန်တော်": "အကိုရေ",
    "ကျွန်မ": "အမရေ",
    # Add more reflections as needed
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

def burmese_chatbot():
    st.title("Burmese Chatbot with You")
    st.write("မင်နဲ့ အမြဲအတူရှိနေမယ့် ဘော့ဘော့လေးပါ ")

    user_input = st.text_input("You:")
    
    if user_input:
        if user_input.lower() == "bye"or "တာ့တာ":
            st.write("Chatbot: Goodbye!")
            break 
        else:
            response = chatbot.respond(user_input)
            st.write("Chatbot:", response)

if __name__ == "__main__":
    burmese_chatbot()
