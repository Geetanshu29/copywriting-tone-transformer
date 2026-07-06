def build_prompt(product_name,
                 product_description,
                 platform,
                 tone):

    prompt = f"""
You are an expert AI copywriter.

Product Name:
{product_name}

Product Description:
{product_description}

Platform:
{platform}

Tone:
{tone}

Generate a high-quality marketing copy.

Guidelines:
- Keep it engaging.
- Use the selected tone.
- Optimize for the selected platform.
- Include a strong call-to-action.
"""

    return prompt