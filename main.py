# main.py
import dalle_api

def main():
    prompt = "A cute baby sea otter"
    image_info = dalle_api.get_dalle_image(prompt)
    print(image_info)

if __name__ == "__main__":
    main()
