import openai
openai.api_key  = "YOUR_API_KEY_IS_HERE"

while True: 
    model = "text-davinci-003"
    user = input("Enter Your Question here: ")

    completion = openai.Completion.create(
    model= "text-davinci-003",
    prompt =  user,
    max_tokens =  1024,
    temperature =  0.5,
    n =  1,
    stop = None
    )
    response = completion.choices[0].text
    print(response)