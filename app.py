import os
from dotenv import load_dotenv
from quart import Quart, request, render_template_string, render_template
import asyncio
from openai import AsyncOpenAI


load_dotenv()
API_KEY = os.getenv("API_KEY")

client = AsyncOpenAI(api_key=API_KEY)
app = Quart(__name__)


@app.route('/', methods=['GET', 'POST'])
async def index():
    if request.method == 'POST':
        form_data = await request.form
        user_input = form_data['user_input']
        results = await asyncio.gather(
            call_openAI1(user_input),
            call_openAI2(user_input),
            call_openAI3(user_input),
            call_openAI4(user_input),
            call_openAI5(user_input),
            call_openAI6(user_input),
            call_openAI7(user_input),
            call_openAI8(user_input),
            call_openAI9(user_input),
            call_openAI11(user_input),
            call_openAI12(user_input),
            call_openAI13(user_input),
            call_openAI14(user_input),
            call_openAI15(user_input),
            call_openAI16(user_input),

        )

        # Process the results
        final_text = '\n\n\n'.join(results) + f'\n сам текст: {user_input} '
        with open('result.txt', 'w') as f:
            f.write(final_text)

        final_results = await asyncio.gather(
            call_final_openAI1(final_text),
            call_final_openAI2(final_text),
            call_final_openAI3(final_text)
        )
        analysis = '\n\n\n'.join(final_results)
        with open('final_results.txt', 'w') as f:
            f.write(analysis)

        return await render_template('index.html', final_text=final_text)

    return await render_template('index.html')


async def call_openAI1(user_input):
    print(f"OpenAI1 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ текста.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Give a list of situations in text;
                                2. Give a list of contexts mentioned in text;
                                3.  Give a list of actors and participants mentioned in text;
                                4. Describe personal and social roles of these actors and participants;
                                5. Describe identities of these actors and participants;
                                6. Describe the affiliation these actors and participants to communities mentioned in text;
                                7. Give well detailed information about background of the story and text;
                                8. Pick up from text high and describe low context communication;
                                9. Identify key themes and topics; 
                                10. Conduct basic narrative analysis; 
                                11. Conduct basic characters analysis; 
                                12. Describe language and rhetoric essentials; 
                                13. Describe context specifics; 
                                14. Make hypothesis about text and author audience and their response; 
                                15. Look at essentials with lens of reader reception theory; 
                                16. Make assumptions about author’s background and intent; 
                                17. Tell me about critical theory applications; 
                                18. Conduct basic thematic framing analysis; 
                                19. Conduct basic semiotics analysis;
                                20. Determine the type of story and give information about this type.
                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI2(user_input):
    print(f"OpenAI2 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий тематический анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Set up a full topic list / Ideas introduced in text
                                2. Give a comprehensive list of thesis statements
                                3. Give me a full list of speech events
                                4. Make a full list of topics mentioned in text
                                5. Catalog themes and counter themes in text
                                6. Examine their frequency and placement of them
                                7. Determine and describe types of that themes
                                8. Describe style and structure of themes being presented in text
                                9. Give a full list of thematic messages
                                10. Evaluate a quality of thematic articulation and resonance, expression, exploration 
                                11. Evaluate thematic significance, richness and depth
                                12. Describe thematic layers and dimensions
                                13. Evaluate thematic flow, dynamics, progression and evolution
                                14. Evaluate thematic cohesion, coherence
                                15. Examine thematic conveyance 
                                16. Evaluate thematic resolution
                                17. Conduct a thematic framing analysis
                                18. Describe symbolic and imagery views on themes in text

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI3(user_input):
    print(f"OpenAI3 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий лингвистический анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Provide me with list of concepts mentioned in text; 
                                2. Look in pattern in how these concepts introduced and developed; 
                                3. Consider semantic roles and and examine their relationships; 
                                4. Make a comprehensive list of semantic fields and give their descriptions; 
                                5. Catalog all cognitive schemes appeared in the text; 
                                6. Catalog all cognitive scenarios appeared in the text; 
                                7. Catalog all cognitive models mentioned in text; 
                                8. Give me a full list of cognitive metaphors; 
                                9. Describe how concepts mentioned in a list of concepts metaphorically constructed; 
                                10. Describe semantic style of the text and evaluate homonymy coefficient, synonymy coefficient, antonymy coefficient, presence vs. absence of enantiosemy;
                                11. Describe semantic structure of the text;
                                12. Catalog conceptual binary oppositions, bipolar evaluation scales used in the text;
                                13. Estimate semantic density of text; 
                                14. Give me a list of the author’s cognitive biases and fallacies identified in the text; 
                                15. Define a basic task of the author’s cognitive process: authorization, evaluative nature, localization, persuasiveness, socialization, etc.;
                                16. Describe an overall author’s cognitive framework.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI4(user_input):
    print(f"OpenAI4 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий текстовый анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                Frames and framing theory.
                                
                                1. Give me full list of frames; 
                                2. Separate list of frames in two categories: thematic and episodic; 
                                3. Distinguish different types of frames and categorise them; 
                                4. Give me a full list of spins; 
                                5. Give me a full list of spins encountered in this text; 
                                6. Analyse frame consistency and evolution within the text; 
                                7. Consider cultural and contextual factors those influencing frames in text.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI5(user_input):
    print(f"OpenAI5 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ текста.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:
                                
                                1. Highlight the main discourse features in text; 
                                2. Identify and describe the types of discourse addressed in the text; 
                                3. Identify all kinds of discourse domains; 
                                4. Give me a full list of discourse markers from text; 
                                5. Describe author’s discourse strategies; 
                                6. Consider discursive constructions in text; 
                                7. Analyse discourse semantics of text;  
                                8. Give me comprehensive list of discursive devices from text and categorize them; 
                                9. Describe discursive construction of knowledge in it; 
                                10. Give me deep description of discourse dynamics; 
                                11. Give a list of discourse points of view; 
                                12. Explore discourse semantics in text; 
                                13. Pick out all discourse modes; 
                                14. Specify discursive repertoire of the author; 
                                15. Make a list of micro-discursive practices; 
                                16. Conduct an analysis of power dynamics in discourses mentioned in text; 
                                17. Provide information about how power dynamics reflect social structures and relationship between characters; 
                                18. Conduct a critical discourse analysis (CDA).

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI6(user_input):
    print(f"OpenAI6 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ текста.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Determine the type of outline and plot structure (incl. argumentative, narrative, expository, explanatory, descriptive etc.); 
                                2. Describe outline and plot organization; 
                                3. Add a description of a plot style; 
                                4. Make a list of plot elements and consider them; 
                                5. Give a type of each plot element; 
                                6. Analyse subplots and threads structure;
                                7. Evaluate clearness and smoothness of outline and plot structure; 
                                8. Examine how many acts in the story plot and describe them;
                                9. Analyse structure of each mentioned act;
                                10. Reflect how every act impact overall story;
                                11. Give me a list of scenes in each act of the story;
                                12.  Reflect how every scene impact their act and overall story;
                                13. Estimate progression of ideas, situations and thoughts in a plot;
                                14. Make full list of subplots and describe them like we did it for the basic outline and structure; 
                                15. Create detailed description of core and circumstances information.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI7(user_input):
    print(f"OpenAI7 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий нарративный анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                Narrative analysis.

                                1. Describe narrative setting;
                                2. Describe overall narrative structure; 
                                3. Determine a type of narrative and describe it; 
                                4. Describe style of narrative and its features; 
                                5. Describe narrative flow and pace; 
                                6. Describe narrative tension;
                                7. Give detailed and structured information about narrator perspectives; 
                                8. Make a full ist of narrative points of view (POV); 
                                9. Consider narrative strategies contained in author’s text; 
                                10. Point out all narrative techniques (incl. structural techniques, engagement techniques, etc.);
                                11. Give me a full list of narrative devices and categorise them; 
                                12. Identify the type of narrative closure;
                                13. Analyse the structural elements of the conclusion including its pacing, climax resolution, final scene etc.;
                                14. Assess how these elements align with or diverge from typical genre conventions;
                                15. Evaluate the conclusion in the context of the text’s genre, considering genre specific expectations for endings;
                                16. Identify elements of narrative closure presented in conclusion (resolution of conflict, character and emotional arcs completion, thematic warp-up, etc.);
                                17. Evaluate effectiveness and completeness of reported closure elements;
                                18. Tell me about stylistic and formal elements connected with closure;
                                19. Examine how conclusion addresses and resolves the central themes of the text;
                                20. Explain intertextual factors connected with the conclusion and narrative closure;
                                21. Assess the clarity and depth of thematic resolution provided;
                                22. Evaluate how the conclusion influences the overall interpretation of the text themes;
                                23. Consider whether the conclusion offers new insights or perspectives on the themes;
                                24. Identify and describe narrative’s underlying messages through the audience’s lenses and from the narrator’s perspective.


                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI8(user_input):
    print(f"OpenAI8 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ текста.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                Storytelling perspective. 
                                
                                1. Provide me with contextual considerations of the story; 
                                2. Describe world building elements of the story;
                                3. Determine the type of story plot;
                                4. Determine the genre of the story script;
                                5. Describe the general dramatic concept of the story;
                                6. Define and describe the control reaction of the scenario;
                                7. Determine the type and assess the level of the leading conflict in history;
                                8. Identify and describe the source and target events;
                                9. Determine the type of dramatic situation;
                                10. Identify and describe the theme and counter-theme of the story script;
                                11. Identify and describe central conflict;
                                12. Identify and describe the type of central conflict in the story scenario;
                                13. Describe type of resolution of the central conflict;
                                14. Describe what the global (transpersonal) goal of the story script is;
                                15. Identify and describe the type of life situation in which the story scenario is realized;
                                16. Identify and describe the original event of the story;
                                17. Give me a full list of characters (highlight protagonist, antagonist and catalyst); 
                                18. Analyse characters arcs and emotional arcs (type, style, structure, list of arc elements, type for each element); 
                                19. Consider characters development techniques; 
                                20. Describe concept of an ensemble of characters; 
                                21. Identify and describe the protagonist, antagonist and catalyst in the text;
                                22. Define the roles of protoganist, antagonist and catalyst;
                                23. Describe the character sculpture, type and number of protoganist, antagonist and catalyst masks;
                                24. Describe the internal and external motifs, motivational structure and goals of the protagonist, antagonist and catalyst;
                                25. Describe protagonist, antagonist and catalyst backgrounds;
                                26. Determine the internal and external motivation of the protagonist, antagonist and catalyst;
                                27. Describe a set of scenario requests/questions from the antagonist and decisions from the protagonist;
                                28. Assess the usefulness (contrast) of the divergence of positions (vectors of goals) in the conflict between main characters;
                                29. Describe and analyze protagonist journey;
                                30. Determine the type of alternative factor that the hero is countering (blow to self-esteem, professional failure, physical harm, threat of death, threat to family life, threat to population life, threat to humanity) and describe it;
                                31. Tell about complications, obstacles and stakes main characters face with;
                                32. Identify and describe the scenario decisions of the protagonist, antagonist and catalyst;
                                33. Look at the structure and give detailed information about the main point, hook, conflict and tension, dramatic concept of the story; 
                                34. Determine the plot and scenario of the story;
                                35. Describe the functions of a story script;
                                36. Describe the structure of a sequence of events in history;
                                37. Identify and describe axial information and related circumstances;
                                38. Identify and describe the structure of gaps and barriers in the story scenario;
                                39. Determine the type of exposure;
                                40. Determine the type of climax;
                                41. Identify and describe exposure control tools and logic;
                                42. Identify and describe the tools, techniques and logic for managing climax;
                                43. Describe the progression of complications, obstacles and stakes within the story;
                                44. Give a look through the audience’s lenses and tell about their potential expectations, theories and subtle clues for them;
                                45. Describe the story system in detail: key details of the image, key details of behavior, climatic details, details of the truth of the body, details of the setting, details of the characters, etc.;
                                46. Identify and describe tools for managing causality, interpretive complexity, and the level of uncertainty in a story scenario;
                                47. Go through all sensory details: give me well detailed and categorised list of them list, designate their connection with the plot structure; 
                                48. Describe the event-behavioral and plot plan of the story;
                                49. Describe the emotional and sensory plan of the story;
                                50. Describe the story's sensory information plan;
                                51. Describe the compositional plan of the story;
                                52. Describe the functional plan of the story;
                                53. Point out subtle vs dramatic changes of the story; 
                                54. Please give me a full list of cathartic tools used by the author
                                55. Give a hypothesis about purposes a story to be written; 
                                56. Give me well reasonable hypotheses about the audience; 
                                57. Please look at the backstory, describe it and its connection with the story; 
                                58. Evaluate the aesthetic unity of the story script
                                Assess the level of detail in the story script
                                59. Analyse instruments those being used for the engagement and persuasiveness of the story;

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI9(user_input):
    print(f"OpenAI9 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ текста.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Describe in detail personal, spatial, temporal deixis
                                2. Describe and analyze discursive, social deixis
                                3. Find, describe and analyze exophoric and endophoric links
                                4. Determine encoding and decoding time according to Fillmore
                                5. Describe the deictic center or Origo
                                6. Describe and analyze the deictic field and deictic narrative
                                7. Describe and analyze deictic projections
                                8. Describe and analyze the deictic system
                                9. Analyse aspects of text, to which the positioning theory can be applied (highlight specifics of personal positioning and subject position); 
                                10. Apply to analysis thematic role theory and do related analysis; 
                                11. Carry out semantic roles labeling; 
                                12. Find out all Identity markers of the author and characters in this text; 
                                13. Describe cultural codes, connected with the author and characters identities;
                                14. Describe narrator perspectives; 
                                15. Provide me with full list of narrator’s points of view; 
                                16. Give me detailed list of actors; 
                                17. Give me a list of their intents (incl. informative, persuasive/argumentative, inspirational/motivational, satirical/ironical, advocacy, speculative, philosophical/metaphysical, therapeutic/healing, descriptive, narrative, provocative, ceremonial, collaborative, experimental, pedagogical, mythological/allegorical, exploratory/expository, expressive/ reflective, analytical/critical, instructional, entertaining etc.) types of intents; 
                                18. Reveal author and character patterns connected with their intents.
                                19. Conduct basic headings and subheadings analysis;
                                20. Evaluate headings and subheadings alignment with the content; 
                                21. Estimate structure, consistency, functionality, transition and flow of headings and subheadings;
                                22. Figure out cross-referencing and keywords of headings and subheadings.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI10(user_input):
    print(f"OpenAI10 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий текстовый анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Describe body paragraphs structure and evaluate its quality; 
                                2. Point out their types (narrative, descriptive, expository or exploratory, persuasive, comparative or contrastive, problem-solution and others); 
                                3. Evaluate paragraphs length, complexity and variety; 
                                4. Explain how paragraphs supporting each text thesis and main idea; 
                                5. Analyse paragraphs alignment with content;

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI11(user_input):
    print(f"OpenAI11 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ текста.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:
                                
                                1. Make full list of author’s arguments; 
                                2. Assess their clarity, precision and strength;
                                3. Describe how author works with credibility and evidence - tell about principles and features he uses for this purpose; 
                                4. Describe author’s argumentative strategies; 
                                5. Evaluate flow and coherence of each argument mentioned in text;
                                6. Give a full list of words and phrases Upgraders and Downgraders and categorise them;
                                7. Assess the contexts in which upgraders and downgraders are used; 
                                8. Evaluate how upgraders and downgraders affects assertiveness in text; 
                                9. Evaluate balance between upgraders and downgraders; 
                                10. Analyse other aspects of assertiveness and pay attention to hedging and boosting in this text.
                                11. Apply speech act theory and related analysis and give overall summary for this text;
                                12. Give a full list of the speech acts used in text: locutionary, perlocutionary and illocutionary;
                                13. Illustrate types of speech acts used by the author: locutionary, illocutionary, perlocutionary with the contexts, themes and text topics, narrator’s perspectives and POVs, narrator’s roles, narrator arguments; 
                                14. Describe utterances functions; 
                                15. Evaluate illocutionary force; 
                                16. Highlight direct vs indirect speech acts; 
                                17. Describe peculiarities of speech act sequencing;
                                18. Give a full list of modalities used in text (optative, hypothetical, potential, intentional, imperative, debitive, modality reality etc.); categorise them;
                                19. Give a full list of transitions used in text (additive, adversative, causal, sequential, exemplifying, comparative, conclusive, temporal, clarification, concession, emphasis) and categorise them;
                                20. Give me a full list of boundary markers used in text and categorise them; 
                                21. Evaluate effectiveness of transitions and boundary markers; 
                                22. Analyse how transitions and boundary markers contribute to the development of text’s themes and main idea;
                                23. Describe speech mannerisms used in text (like hesitation indicators, self-correction mechanisms, emphasis amplifiers, discourse markers, affirmation and agreement, politeness formula, elicitation devices, narrative enhancers, idiosyncratic expressions, questioning mechanisms, contrastive markers, temporal markers, causal connections, inclusive language, exclamations and interjections, figurative language, qualifiers and modifiers, code-switching, hedging, reference switching, directives etc); 
                                24. Conduct basic semantic collocation analysis; 
                                25. Find out author’s orientation in time and describe it; 
                                26. Describe author’s usage of time in text; 
                                27. Give a list af temporal markers used in text; 
                                28. Evaluate pacing and temporal flow; 
                                29. Distinguish between chronological and non-chronological narration; 
                                30. Analyse how author uses flashbacks, foreshadowing, nonlinear timelines and their effect on the story’s pace and suspense; 
                                31. Consider how time is used as a thematic element; 
                                32. Describe other peculiarities of use of time;
                                33. Conduct basic analysis of cohesion (lexical, grammatical) and coherence (logical, tone and style, thematic unity) of this text;
                                34. Apply cohesion and coherence theory to our analysis; 
                                35. Describe overall narrative logic; 
                                36. Connect themes and messages distribution with overall narrative logic; 
                                37. Evaluate logical flow and consistency of ideas; 
                                38. Evaluate logic structure of the text and describe types, features, number, and frequency of logical constructions used;
                                39. Describe number and depth of nested cause-effect chains used in text;
                                40. Tell me about types, number, and frequency of logical operators used in the text;
                                41. Describe cohesive devises used in the text (Cause and Effect Connectors, Comparison and Contrast Connectors, Exemplification, Reformulation, Summation, Pronominal Reference, Collocation and its patterns, Time Connectors, Spatial Connectors, Intensifiers and Emphasis, Modality, Concessive Connectors, Listing or Sequencing, Interjections, Anaphoric and Cataphoric Reference etc); 
                                42. Evaluate thematic unity in the text; 
                                43. Evaluate overall tone and style consistency of the story.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI12(user_input):
    print(f"OpenAI12 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий морфологический анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Describe author’s diction / word choice;
                                2. Describe style of vocabulary; 
                                3. Conduct deep morphological analysis; 
                                4. Create parts of speech vocabularies incl. modals and conditionals and usage of them; 
                                5. Estimate language complexity (incl. common/unusual language) length and probability, variety; 
                                6. Conduct connotations and denotations analysis; 
                                7. Evaluate level of language formality; 
                                8. Evaluate use of non-standard language; 
                                9. Apax legomena - make dictionary of words appeared only once in a text; 
                                10. Make a vocabulary of multi syllable words; 
                                11. Tell me about abstract and concrete language; 
                                12. Analyse other metrics of linguistic repertoire;
                                13. Analyse sentence structure and clause usage; 
                                14. Apply an analysis of lexico-functional grammar (LFG); 
                                15. Apply an analysis of construction grammar; 
                                16. Apply an analysis of role grammar theory and role and reference grammar (RRG); 
                                17. Apply an analysis of theory of syntactic functions; 
                                18. Apply control theory to our analysis;
                                19. Evaluate sentences length and describe peculiarities of it;
                                20. Examine sentences types in text and describe them;
                                21. Estimate variety and complexity of syntax structures;
                                22. Identify and describe word order structures;
                                23. Examine parallelism of syntax structures;
                                24. Describe deep syntax structures in a step-by-step manner: first - types of sentences, second - hierarchical organization of the sentence, third - syntactic structure of the sentence, fourth - types of syntax structures, fifth - length, probability, complexity and variety; 
                                25. Describe transformational rules, their types and variety used by author; 
                                26. Describe punctuation peculiarities and their effect to narrative flow and structure, syntax structure;
                                27. Extract active and passive voice constructions and describe them;
                                28. Evaluate text density;
                                29. Describe peculiarities of the author’s use of white space;
                                30. Analyse typographical, lexical and syntactic errors;
                                31. Estimate overall author’s pragmatic competence.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI13(user_input):
    print(f"OpenAI13 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий текстовый анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Please basically describe mood, feelings and atmosphere in text; 
                                2. Give me full list of emotives and affectives mentioned in text;
                                3. Give me well detailed list of sentiment devices with a description of each of them; 
                                4. Define types of sentiment in this text;
                                5. Analyse what emotions are evoked, suggested or suppressed in text;
                                6. Conduct an analysis of emotional intelligence elements in text;
                                7. Give me list of figurative and symbolic language used by the author in text; 
                                8. Define types of figurative and symbolic language and describe each of the type you’ve mentioned;
                                9. Please give me list of literary and rhetorical devices used by the author in text; 
                                10. Define types of literary and rhetorical devices and describe each type.
                                
                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI14(user_input):
    print(f"OpenAI14 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий текстовый анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:
                                
                                1. Research the author’s philosophical, cultural and historical background;
                                2. Give me a full list of philosophical themes and questions posed in text;
                                3. Give me a list of epistemological, metaphysical and existential questions posed in text;
                                4. Determine arguments presented for each philosophical theme and question;
                                5. Note use of specific philosophical concepts and ideas;
                                6. Determine if text somehow aligns with specific philosophical traditions or schools of thoughts;
                                7. Recognise potential influences to the author of philosophers and philosophical works;
                                8. Consider the ethical dimensions and moral implications of the text;
                                9. Evaluate the premises, the applicability of ethical frameworks, and the implications for real-world ethical dilemmas;
                                10. Determine the philosophical methodology used by the author;
                                11. Look for any contradictions within the text or controversial positions the author takes.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI15(user_input):
    print(f"OpenAI15 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий текстовый анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                               1. Look at this text through the lens of interactional analysis and give me an additions to our analysis;
                                2. Look at this text through the lens of conversasion analysis and give me an additions to our analysis;
                                3. Look at this text through the lens of reader-response theory and give me an additions to our analysis;
                                4. Look at this text through the lens of rhetorical analysis and give me an additions to our analysis;
                                5. Look at this text through the lens of stylistic theory and give me an additions to our analysis;
                                6. Look at this text through the lens of formalism theory and give me an additions to our analysis;
                                7. Look at this text through the lens of structuralism theory and give me an additions to our analysis;
                                8. Look at this text through the lens of semiotics theory and give me an additions to our analysis;
                                9. Look at this text through the lens of psychoanalytic literary theory and give me an additions to our analysis;

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_openAI16(user_input):
    print(f"OpenAI16 called")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий текстовый анализ.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                Stylometry.
                                
                                1. Evaluate and describe a pace of the story; 
                                2. Give me detailed information about meter, rhythm and it’s schemes; 
                                3. Define sound patterns from text; 
                                4. Provide me with detailed information of tone; 
                                5. Tell me about types of tones in this text; 
                                6. Consider types of tones consistency and shifts; 
                                7. Analyse purpose of types of tones usage;
                                8. Tell me about style and tone interactions;
                                9. Consider different speech registers;
                                10. Conduct an analysis for aesthetic qualities mentioned in text;
                                11. Analyse style consistency of the author and tell me about peculiarities in it;
                                12. Point out rhyme, genre and jargon specifics of the author style;

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=2048,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_final_openAI1(user_input):
    print(f"User Input: {user_input}")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ пациента основываясь на предыдущих заключениях.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                                1. Tell me about tacit knowledge (unspoken understanding) could be recognised in this text;
2. Analyse all cases where irony or sarcasm used in text to implicate something more than explained;
3. Look at recurring ideas, motifs and themes that might not be explicitly stated but are suggested through repetition, contrast or parallels;
4. Examine objects, characters, settings, or actions that could symbolize larger concepts or ideas;
5. Tell me additional information about implicit ideas which are contained in the text;
6. Tell me about implications which are contained in text;

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=4096,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_final_openAI2(user_input):
    print(f"User Input: {user_input}")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ пациента основываясь на предыдущих заключениях.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                               1. Find out all semantic binary oppositions used by author in text;
2. Conduct well detailed subtext analysis based on whole analysis we’ve done before.

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=4096,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


async def call_final_openAI3(user_input):
    print(f"User Input: {user_input}")

    response = await client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "user",
                "content": f"""Ты профессиональный психолингвист совершающий анализ пациента основываясь на предыдущих заключениях.
                                Твоя задача на основе текста пациента сделать выводы по следующим темам:

                               1. Estimate risk appetite of the author;
2. Evaluate author’s tolerance to uncertainty;
3. Give me a full list of values posed in text by the author; 
4. Give me a full list of coping strategies related to author’s values;
5. Give me a full list of motifs of the author; 
6. Analyse what author’s beliefs encountered in text; 
7. Provide me with list of attitudes of the author and text characters; 
8. Give detailed list author and characters opinions; 
9. Give me list of author and characters assumptions and judgements; 
10. Provide me with list of author and characters presuppositions and categorize them by their type; 
11. Make a list of authors and characters choices (incl. moral and ethical choices); 
12. Analyse the implicatures used by the author into the text; 
13. Tell me about philosophical underpinnings of the author; 
14. Describe Predominant Behavior Type appeared in text: appetitive, avoidance, defensive, exploratory, territorial, assimilative, exploratory (investigating external conditions), accommodative (adapting to external conditions), organizational (productive change in external conditions), aggressive (unproductive change in external conditions, destruction), and others types of behaviors;
15. Describe Socio-Economic Games appeared in text: zero-sum game vs. non-zero-sum game, cooperative game vs. competitive game, full-information game vs. incomplete-information game, etc.;
16. Identify and describe external and internal conflicts of the author and text characters; 
17. Consider existential problems according to I. Yalom related to the author and text characters; 
18. Conduct ego-states analysis of the author and text characters; 
19. Conduct ego-states dynamic analysis through the narration; 
20. Provide with information of racket system analysis; 
21. Apply moral development theories (incl. Kohlberg’s stages) to our analysis;
22. Look at the text through the lenses of BIG5 (OCEAN) psychometric model using all scales and sub-scales of it;
23. Look at the text through the lenses of HEXACO psychometric model using all scales and sub-scales of it;
24. Look at the text through the lenses of MMPI psychometric model using all scales of it;
25. Look at the text through the lenses of Operationalized Psychodynamic Diagnostics, point out and rank all Repetitive-Dysfunctional Conflicts of the author;
26. List, describe and assess all author’s early and late psychic defense mechanisms according to Nancy McWilliams and other authors;
27. Assess the likelihood that the author of the text has the following thinking disorders: ****reduction in generalization level, distortion of the generalization process, multidimensional thinking, critical thinking loss, reasoning, circumstantiality, inertia, lability, acceleration, jumpiness, fragmentation, slowing, mentism, sperre, concrete thinking, thematic slipping, incoherence, paralogical thinking, verbigeration, speech stereotypes, coprolalia, obsessive thoughts, obsessions, compulsions, overvalued ideas, primary and figurative delusions;
28. Describe congnitive style characteristics and metrics:
    1. Characteristic of Field relation. Metrics: field-dependence vs. field-independence;
    2. Characteristic of Representational Systems. Metrics: types, features, number, and frequency of different forms of representations;
    3. Characteristic of the Leading Functional Sphere. Metrics: orientation on perception and sensations, sensual and emotional evaluation, thinking and cognitive evaluation, pragmatic actions;
    4. Characteristic of Intelligence Structure. Metrics: form of intelligence (visual-imaginative, verbal-lexical, computational or logical-mathematical, bodily-kinesthetic, spatial, social or interpersonal, intrapersonal, emotional, adaptive), features, and presumed level of development;
    5. Characteristic of Thinking Level. Metrics: field (does not differentiate objects, emphasizes background), object (differentiates and describes shape and properties of objects), concrete (describes goals and logic of pragmatic use of objects), conceptual (capable of identifying unity of essential properties, relations, and connections of objects or phenomena, generalizing objects of a certain class according to specific common features), rational (describes personal sensations and expresses personal attitude towards objects and results of their use, capable of asserting or denying about an object, its properties or relations between objects), symbolic (capable of symbolizing objects and activities, forming analogies and demonstrating ability for metaphorical transfer), sign (integrates various levels of thinking in real activity), conceptual (describes integration of sign level, mental operations with signs, and mental independent modeling of situations and all aspects of one's activity);
    6. Characteristic of Locus of Control. Metrics: internal locus of control vs. external locus of control;
    7. Characteristic of Activity Level. Metrics: activity vs. passivity;
    8. Characteristic of Self-Regulation Type. Metrics: impulsivity, reactivity, bottom-up self-regulation vs. reflectiveness, proactivity, top-down self-regulation;
    9. Characteristic of Tolerance to Uncertainty. Metrics: low vs. high tolerance to uncertainty;
    10. **Characteristic of Exposition Structuring Level.** Metrics: high level of informational entropy vs. low level of informational entropy;
    11. Characteristic of Standardization Level. Metrics: originality, uniqueness, creativity, innovation vs. commonality, stereotypicality, adherence to standards, adaptability;
    12. Characteristic of Level of Detail. Metrics: focusing control, attention to multiple aspects of the situation and objective details vs. scanning control, superficiality, attention to overt and exaggerated characteristics and properties;
    13. Characteristic of Information Processing Style. Metrics: smoothing, generalization, focus on similarities, simplification, and syntheticity vs. sharpening, detailing, emphasis on differences and distinctive features, analyticity;
    14. Characteristic of Focus Level. Metrics: ability to generate multiple ideas vs. meticulousness, the pursuit of thorough and deep elaboration of a single idea;
    15. Characteristic of Cognitive Process Stability. Metrics: spontaneity vs. sequentiality;
    16. Characteristic of Cognitive Process Complexity. Metrics: cognitive simplicity vs. cognitive complexity;
    17. Characteristic of Cognitive Process Fluidity. Metrics: fluency, unrestrainedness vs. inhibitedness, process looping;
    18. Characteristic of Cognitive Control Type. Metrics: cognitive rigidity vs. cognitive flexibility;
    19. Characteristic of the Cognitive Process Source. Metrics: discursiveness vs. intuitiveness;
    20. Characteristic of Cognitive Process Orientation. Metrics: impressiveness vs. expressiveness;
    21. Characteristic of Environmental Integration. Metrics: assimilative style vs. exploratory style;
    22. Characteristic of Preferred Argumentation Type. Metrics: concreteness, reliance on facts vs. abstractness, reliance on arguments;
    23. Characteristic of Preferred Exposition Structure. Metrics: recursion vs. sequentiality;

                                Проанализируй текст ниже используя вопросы сверху
                                {user_input}
                                """
            }
        ],
        temperature=0.3,
        max_tokens=4096,
        top_p=0.2,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )

    final_text = response.choices[0].message.content
    return final_text


if __name__ == '__main__':
    app.run()
