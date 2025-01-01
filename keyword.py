keyword: str = "pomeranč"
why_i_am_the_right_candidate: str = """
Jsem v podstatě python junior nadšenec, který se chce naplno věnovat tomu, 
co ho baví, a to nejen doma ve volných chvílích, ale i v práci. A protože to 
myslím vážně a kvalita kódu je pro mě číslo 1, proplouvám sedmiměsíčním 
kurzem Python developera. V součastnosti bohužel ještě nemám hotový vlastní 
projekt. Jinak ráda pracuji a řeším úkoly v týmu i samostatně, 
jsem přátelská, učenlivá, spolehlivá a mám ráda pomeranč.
"""


def contain_keyword(text: str, word: str) -> bool:
    """
    Funkce vyhledává v textu klíčové slovo

    :param text: libovolný text
    :param word: klíčové slovo
    :return: True/False
    """
    # word = str(slovo)
    return word.lower() in text.lower()


if contain_keyword(why_i_am_the_right_candidate, keyword):
    print(f"Žadatel splnil zadání. Text obsahuje klíčové slovo '{keyword}'.")
else:
    print(f"Je mi líto, ale zadané klíčové slovo '{keyword}' text neobsahuje.")
