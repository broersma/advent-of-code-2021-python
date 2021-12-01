def _get_sample_and_answer(day, year):
    r"""
    >>> import requests_cache
    >>> requests_cache.install_cache('doctest_get_sample_and_answer_cache')
    >>> _get_sample_and_answer(1, 2020)[0]
    '1721\n979\n366\n299\n675\n1456'
    >>> _get_sample_and_answer(1, 2020)[1]
    '514579'
    >>> _get_sample_and_answer(2, 2020)[0]
    '1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc'
    >>> _get_sample_and_answer(2, 2020)[1]
    '2'
    >>> _get_sample_and_answer(3, 2020)[0]
    '..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#'
    >>> _get_sample_and_answer(3, 2020)[1]
    '7'
    >>> _get_sample_and_answer(4, 2020)[0]
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm\n\niyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929\n\nhcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm\n\nhcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in'
    >>> _get_sample_and_answer(4, 2020)[1]
    '2'
    >>> _get_sample_and_answer(5, 2020)[0]
    'FBFBBFFRLR'
    >>> _get_sample_and_answer(5, 2020)[1]
    '357'
    >>> _get_sample_and_answer(6, 2020)[0]
    'abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb'
    >>> _get_sample_and_answer(6, 2020)[1]
    '11'
    >>> _get_sample_and_answer(7, 2020)[0]
    'light red bags contain 1 bright white bag, 2 muted yellow bags.\ndark orange bags contain 3 bright white bags, 4 muted yellow bags.\nbright white bags contain 1 shiny gold bag.\nmuted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\nshiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\ndark olive bags contain 3 faded blue bags, 4 dotted black bags.\nvibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\nfaded blue bags contain no other bags.\ndotted black bags contain no other bags.'
    >>> _get_sample_and_answer(7, 2020)[1]
    '4'
    >>> _get_sample_and_answer(8, 2020)[0]
    'nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6'
    >>> _get_sample_and_answer(8, 2020)[1]
    '5'
    >>> _get_sample_and_answer(9, 2020)[0]
    '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576'
    >>> _get_sample_and_answer(9, 2020)[1]
    '127'
    >>> _get_sample_and_answer(10, 2020)[0]
    '16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4'
    >>> _get_sample_and_answer(10, 2020)[1]
    '7'
    >>> _get_sample_and_answer(11, 2020)[0]
    'L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL'
    >>> _get_sample_and_answer(11, 2020)[1]
    '37'
    """
    import requests
    import bs4
    url = "https://adventofcode.com/{0}/day/{1}".format(year, day)
    with open('cookie.txt', 'r') as cookie:
        session_string = cookie.read().strip()
        if session_string.startswith("session="):
            session = session_string[8:]
    response = requests.get(
        url,
        headers={"User-Agent": "little_helper.py/v1"},
    )
    if not response.ok:
        raise RuntimeError("Non-200 response for POST: {}".format(response))
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    sample_tag = soup.select('pre code')[0]
    sample = sample_tag.string.strip()
    answer_tags = [tag for tag in soup.select('em code,code em') if tag.sourceline > sample_tag.sourceline or (tag.sourceline == sample_tag.sourceline and tag.sourcepos > sample_tag.sourcepos)]
    answer_tag = answer_tags[0]
    answer = answer_tag.string.strip()
    return sample, answer


def get_input(day, year):

    if not (1 <= day <= 25):
        raise ValueError(f"day must be between 1 and 25 inclusive, is {day}")

    if not (2015 <= year <= 2999):
        raise ValueError(f"year must be between 2015 and 2999 inclusive, is {year}")

    import os

    cache_file_name = 'day{0}.txt'.format(day)

    if not os.path.isfile(cache_file_name):
        import urllib.request
        import shutil

        url = "https://adventofcode.com/{0}/day/{1}/input".format(year, day)
        req = urllib.request.Request(url)

        # cookie.txt should be in your .gitignore and contain 'session=<your advent of code session id>'
        with open('cookie.txt', 'r') as cookie:
            req.add_header('Cookie', cookie.read().strip())

        try:
            with urllib.request.urlopen(req) as input, open(cache_file_name, 'wb') as output:
                shutil.copyfileobj(input, output)
        except urllib.error.HTTPError:
            return

    with open(cache_file_name, 'rb') as input:
        return input.read().decode("utf-8").rstrip()
