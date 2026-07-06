from prompt import build_prompt
from api import generate_copy

print("=" * 50)
print(" AI Copywriting & Tone Transformer ")
print("=" * 50)

product_name = input("\nProduct Name : ")

description = input("Product Description : ")

platform = input(
    "Platform (LinkedIn / Instagram / Email) : "
)

tone = input(
    "Tone (Professional / Funny / Friendly / Persuasive) : "
)

temperature = float(
    input("Temperature (0-1) : ")
)

top_p = float(
    input("Top P (0-1) : ")
)

prompt = build_prompt(
    product_name,
    description,
    platform,
    tone
)

print("\nGenerating Copy...\n")

try:

    result = generate_copy(
        prompt,
        temperature,
        top_p
    )

    print("=" * 50)
    print(result)
    print("=" * 50)

except Exception as e:

    print("\nError:")
    print(e)