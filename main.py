from gtts import gTTS 
def create(text, filename):
  tts = gTTS(text)
  tts.save(filename)

if __name__ == "__main__":
  text = input("Enter your text")
  filename = input("Enter filename")
  create(text, filename)
  print("created {0}".format(filename))
