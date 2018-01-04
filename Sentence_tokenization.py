import re, pickle, numpy as np

def find(s, chs):
    temp=[]
    for ch in chs:
        temp+=[i for i, ltr in enumerate(s) if ltr == ch]
    return temp

def int_to_8bit_binary(inp):
    # if inp > 255:
    #     print "Not an ascii character !!"
    #     return -1
    inp = ord(inp)
    temp = []
    while inp > 1:
        temp.append(inp % 2)
        inp = int(inp/2)
    temp.append(1)
    if len(temp) < 8:
        temp += [0 for i in range(8-len(temp))]
    return list(reversed(temp))

# softmax activation function
def softmax(x):
    x = np.where(x > 50, 50, x)
    x = np.where(x < -50, -50, x)
    sum = np.sum(np.exp(x))
    t = np.exp(x) / sum
    return t

def pridect(x):
    w = pickle.load(open('weights.pickle', 'rb'))
    vh = np.dot(w[0], x)
    h = np.where(vh < 0, 0, vh)
    o = softmax(np.dot(w[1], h))
    return o

# just use this function
def nn_sent_tokenizer(text):
    text = re.sub(r'\n|\t|[^\x00-\x7F]', r'', text)
    indexs = find(text, '.;')
    context = 5

    sent_end = []
    for i in indexs:
        a = text[i - context:i]+text[i+1:i + context + 1]
        if len(a) < 10:
            a += ''.join([' ' for l in range(10-len(a))])
        binary = []
        for j in a:
            binary += int_to_8bit_binary(j)
        if pridect(binary)[0] == 1:
            sent_end.append(i+1)
    lines = []
    i0=0
    if sent_end:
        for i1 in sent_end:
            lines.append(text[i0:i1])
            i0=i1
    return lines

if __name__ == "__main__":
    text = '''
                Tyrus Wong, Bambi Artist Thwarted by Racial Bias, Dies at 106 - The New York Times,New York Times,Margalit Fox,2017-01-06,2017.0,1.0,,"When Walt Disneys Bambi opened in 1942, critics praised its spare, haunting visual style, vastly different from anything Disney had done before. But what they did not know was that the films striking appearance had been created by a Chinese immigrant artist, who took as his inspiration the landscape paintings of the Song dynasty. The extent of his contribution to Bambi, which remains a   mark for film animation, would not be widely known for decades. Like the films title character, the artist, Tyrus Wong, weathered irrevocable separation from his mother --  and, in the hope of making a life in America, incarceration, isolation and rigorous interrogation --  all when he was still a child. In the years that followed, he endured poverty, discrimination and chronic lack of recognition, not only for his work at Disney but also for his fine art, before finding acclaim in his 90s. Mr. Wong died on Friday at 106. A Hollywood studio artist, painter, printmaker, calligrapher,   illustrator and, in later years, maker of fantastical kites, he was one of the most celebrated   artists of the 20th century. But because of the marginalization to which   were long subject, he passed much of his career unknown to the general public. Artistic recognition, when Mr. Wong did find it, was all the more noteworthy for the fact that among Chinese immigrant men of his generation, professional prospects were largely limited to menial jobs like houseboy and laundryman. Trained as a painter, Mr. Wong was a leading figure in the Modernist movement that flourished in California between the first and second World Wars. In 1932 and again in 1934, his work was included in group shows at the Art Institute of Chicago that also featured Picasso, Matisse and Paul Klee. As a staff artist for Hollywood studios from the 1930s to the 1960s, he drew storyboards and made vibrant paintings, as detailed as any architectural illustrations, that helped the director envision each scene before it was shot. Over the years his work informed the look of animated pictures for Disney and   films for Warner Brothers and other studios, among them The Sands of Iwo Jima (1949) Rebel Without a Cause (1955) and The Wild Bunch (1969). But of the dozens of films on which he worked, it was for Bambi that Mr. Wong was --  belatedly --  most renowned. He was truly involved with every phase of production, John Canemaker, an   animator and a historian of animation at New York University, said in an interview for this obituary in March. He created an art direction that had really never been seen before in animation.  In 2013 and 2014, Mr. Wong was the subject of Water to Paper, Paint to Sky, a major retrospective at the Disney Family Museum in San Francisco. From the museums windows, which overlook San Francisco Bay, he could contemplate Angel Island, where more than nine decades earlier, as a lone    he had sought to gain admission to a country that adamantly did not want him. Wong Gen Yeo (the name is sometimes Romanized Wong Gaing Yoo) was born on Oct. 25, 1910, in a farming village in Guangdong Province. As a young child, he already exhibited a love of drawing and was encouraged by his father. In 1920, seeking better economic prospects, Gen Yeo and his father embarked for the United States, leaving his mother and sister behind. Gen Yeo would never see his mother again. They were obliged to travel under false identities --  a state of affairs known among Chinese immigrants as being a paper son --  in the hope of circumventing the Chinese Exclusion Act of 1882. Signed into law by President Chester A. Arthur, the act, which drastically curtailed the number of Chinese people allowed to enter the country, was among the earliest United States laws to impose severe restrictions on immigration. But in 1906, an unforeseen loophole opened in the form of the San Francisco earthquake and fire. Because a huge number of municipal documents, including birth and immigration records, were destroyed, many newly arrived Chinese capitalized on the loss, maintaining that they had been born in San Francisco before the fire. As United States citizens, they were entitled to bring over their relatives --  or, in the case of Gen Yeo and his father, paper sons posing as relatives. Attuned to the deception, United States immigration officials put Chinese arrivals through a formidable inquisition to ensure they were who they claimed to be. The questions came like gunfire: In which direction does your village face? How many windows are in your house? Where in the house is the rice bin? How wide is your well? How deep? Are there trees in your village? Are there lakes? What shops can you name? The sponsoring relative was interrogated separately, and the answers had to match. For the new arrival, a major mistake, or a series of smaller ones, could mean deportation. To stand a chance of passing, aspirants memorized rigorous dossiers known as coaching papers. The ensuing interrogation was hard enough for adults.    Gen Yeo would undergo it alone. On Dec. 30, 1920, after a month at sea, the Wongs landed at Angel Island Immigration Station. The elder Mr. Wong was traveling as a merchant named Look Get his son as Look Tai Yow. Angel Island is considered to be the Ellis Island of the West Coast, Lisa See, the author of On Gold Mountain (1995) a nonfiction chronicle of her   family, said in an interview in 2016. However, she continued: The goal was really very different than Ellis Island, which was supposed to be so welcoming. Angel Island opened very specifically to keep the Chinese out.  Because Mr. Wongs father had previously lived in the United States as Look Get, he was able to clear Immigration quickly. But as a new arrival, Gen Yeo was detained on the island for nearly a month, the only child among the immigrants being held there. I was scared half to death I just cried, Mr. Wong recalled in Tyrus, an   documentary directed by Pamela Tom, which premiered in 2015. Every day is just miserable --  miserable. I hated that place.  On Jan. 27, 1921, in the presence of an interpreter and a stenographer, young Gen Yeo, posing as Look Tai Yow, was interrogated by three inspectors. His father had already been questioned. Gen Yeo was well prepared and answered without error. In Sacramento, where he joined his father, a schoolteacher Americanized Tai Yow to Tyrus, and he was known as Tyrus Wong ever after. Soon afterward, father and son were separated once more, when the elder Mr. Wong moved to Los Angeles to seek work. For reasons that have been lost to time, he could not take his son. Tyrus lived on his own in a Sacramento boardinghouse while attending elementary school. Two years later --  possibly more --  Tyrus traveled to Los Angeles to join his father, who had found work in a gambling den. They lived in a   boardinghouse sandwiched between a butcher shop and a brothel. After school, Tyrus worked as a houseboy for two Pasadena families, earning 50 cents a day. His first art teacher was his father, who trained him nightly in calligraphy by having him dip a brush in water and trace ghostly characters on newspaper: They could not afford ink or drawing paper. When Tyrus was in junior high, a teacher, noting his drawing talent, arranged a summer scholarship to the Otis Art Institute in Los Angeles. By his own account an indifferent student in public school, Tyrus found his calling at the institute, now the Otis College of Art and Design. When his scholarship ended he declined to return to junior high. His father scraped together the $90 tuition --  a small fortune --  to let him stay on as Otiss youngest student. He studied there for at least five years, simultaneously working as the school janitor, before graduating in the 1930s. Not long afterward his father died, leaving young Mr. Wong entirely on his own. From 1936 to 1938, Mr. Wong was an artist for the Works Progress Administration, creating paintings for libraries and other public spaces. With friends, including the   artist Benji Okubo, he founded the Oriental Artists Group of Los Angeles, which organized exhibitions of members work --  an   level of exposure for Asian artists at the time. Mr. Wong, newly married and needing steady work, joined Disney in 1938 as an  creating the thousands of intermediate drawings that bring animated sequences to life. Asians were then a novelty at Hollywood studios, and Mr. Wong was made keenly aware of the fact, first at Disney and later at Warner Brothers. One   flung a racial epithet at him. Another assumed on sight that he worked in the company cafeteria. Then there was the affront of the  s job itself: Painstaking, repetitive and for Mr. Wong quickly   it is the   work of animation --  a terrible use of his talents as a landscape artist and a painter, Mr. Canemaker said. A reprieve came in the late 1930s, when Mr. Wong learned that Disney was adapting Bambi, a Life in the Woods, the 1923 novel by the Austrian writer Felix Salten about a fawn whose mother is killed by a hunter. In trying to animate the book, Disney had reached an impasse. The studio had enjoyed great success in 1937 with its animated film Snow White and the Seven Dwarfs, a baroque production in which every detail of the backgrounds --  every petal on every flower, every leaf on every tree --  was meticulously represented. In an attempt to use a similar style for Bambi, it found that the ornate backgrounds camouflaged the deer and other forest creatures on which the narrative centered. Mr. Wong spied his chance. I said, Gee, this is all outdoor scenery, he recalled in a video interview years afterward, adding: I said, Gee, Im a landscape painter!  Invoking the exquisite landscape paintings of the Song dynasty (A. D. 960-- 1279) he rendered in watercolors and pastels a series of nature scenes that were moody, lyrical and atmospheric --  at once lush and spare --  with backgrounds subtly suggested by a stroke or two of the brush. Walt Disney went crazy over them, said Mr. Canemaker, who wrote about Mr. Wong in his book Before the Animation Begins: The Art and Lives of Disney Inspirational Sketch Artists (1996). He said, I love this indefinite quality, the mysterious quality of the forest.  Mr. Wong was unofficially promoted to the rank of inspirational sketch artist. But he was more than that, Mr. Canemaker explained. He was the designer he was the person they went to when they had questions about the color, about how to lay something out. He even influenced the music and the special effects: Just by the look of the drawings, he inspired people.  Mr. Wong spent two years painting the illustrations that would inform every aspect of Bambi.  Throughout the finished film --  lent a brooding quality by its stark landscapes misty, desaturated palette and figures often seen in silhouette --  his influence is unmistakable. But in 1941, in the wake of a bitter employees strike that year, Disney fired Mr. Wong. Though he had chosen not to strike --  he felt the studio had been good to him, Mr. Canemaker said --  he was let go amid the lingering climate of   resentments. On Bambi, Mr. Wongs name appears, quite far down in the credits, as a mere background artist. Mr. Wong joined Warner Brothers in 1942, working there --  and lent out on occasion to other studios --  until his retirement in 1968."
            '''
    lines = nn_sent_tokenizer(text)
    for line in lines:
        print line