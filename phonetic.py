import re


codes = {
    'A': {
        0: (0, -1, -1),
        'I': {0: (0, 1, -1)},
        'J': {0: (0, 1, -1)},
        'Y': {0: (0, 1, -1)},
        'U': {0: (0, 7, -1)}
    },
    'B': {0: (7, 7, 7)},
    'C': {
        0: (5, 5, 5),
        1: (4, 4, 4),
        'Z': {
            0: (4, 4, 4),
            'S': {0: (4, 4, 4)}
        },
        'S': {
            0: (4, 4, 4),
            'Z': {0: (4, 4, 4)}
        },
        'K': {
            0: (5, 5, 5),
            1: (45, 45, 45)
        },
        'H': {
            0: (5, 5, 5),
            1: (4, 4, 4),
            'S': {0: (5, 54, 54)}
        }
    },
    'D': {
        0: (3, 3, 3),
        'T': {0: (3, 3, 3)},
        'Z': {
            0: (4, 4, 4),
            'H': {0: (4, 4, 4)},
            'S': {0: (4, 4, 4)}
        },
        'S': {
            0: (4, 4, 4),
            'H': {0: (4, 4, 4)},
            'Z': {0: (4, 4, 4)}
        },
        'R': {
            'S': {0: (4, 4, 4)},
            'Z': {0: (4, 4, 4)}
        }
    },
    'E': {
        0: (0, -1, -1),
        'I': {0: (0, 1, -1)},
        'J': {0: (0, 1, -1)},
        'Y': {0: (0, 1, -1)},
        'U': {0: (1, 1, -1)}
    },
    'F': {
        0: (7, 7, 7),
        'B': {0: (7, 7, 7)}
    },
    'G': {0: (5, 5, 5)},
    'H': {0: (5, 5, -1)},
    'I': {
        0: (0, -1, -1),
        'A': {0: (1, -1, -1)},
        'E': {0: (1, -1, -1)},
        'O': {0: (1, -1, -1)},
        'U': {0: (1, -1, -1)}
    },
    'J': {0: (4, 4, 4)},
    'K': {
        0: (5, 5, 5),
        'H': {0: (5, 5, 5)},
        'S': {0: (5, 54, 54)}
    },
    'L': {0: (8, 8, 8)},
    'M': {
        0: (6, 6, 6),
        'N': {0: (66, 66, 66)}
    },
    'N': {
        0: (6, 6, 6),
        'M': {0: (66, 66, 66)}
    },
    'O': {
        0: (0, -1, -1),
        'I': {0: (0, 1, -1)},
        'J': {0: (0, 1, -1)},
        'Y': {0: (0, 1, -1)}
    },
    'P': {
        0: (7, 7, 7),
        'F': {0: (7, 7, 7)},
        'H': {0: (7, 7, 7)}
    },
    'Q': {0: (5, 5, 5)},
    'R': {
        0: (9, 9, 9),
        'Z': {0: (94, 94, 94), 1: (94, 94, 94)},  # special case
        'S': {0: (94, 94, 94), 1: (94, 94, 94)}   # special case
    },
    'S': {
        0: (4, 4, 4),
        'Z': {
            0: (4, 4, 4),
            'T': {0: (2, 43, 43)},
            'C': {
                'Z': {0: (2, 4, 4)},
                'S': {0: (2, 4, 4)}
            },
            'D': {0: (2, 43, 43)}
        },
        'D': {0: (2, 43, 43)},
        'T': {
            0: (2, 43, 43),
            'R': {
                'Z': {0: (2, 4, 4)},
                'S': {0: (2, 4, 4)}
            },
            'C': {
                'H': {0: (2, 4, 4)}
            },
            'S': {
                'H': {0: (2, 4, 4)},
                'C': {
                    'H': {0: (2, 4, 4)}
                }
            }
        },
        'C': {
            0: (2, 4, 4),
            'H': {
                0: (4, 4, 4),
                'T': {
                    0: (2, 43, 43),
                    'S': {
                        'C': {
                            'H': {0: (2, 4, 4)}
                        },
                        'H': {0: (2, 4, 4)}
                    },
                    'C': {
                        'H': {0: (2, 4, 4)}
                    }
                },
                'D': {0: (2, 43, 43)}
            }
        },
        'H': {
            0: (4, 4, 4),
            'T': {
                0: (2, 43, 43),
                'C': {
                    'H': {0: (2, 4, 4)}
                },
                'S': {
                    'H': {0: (2, 4, 4)}
                }
            },
            'C': {
                'H': {0: (2, 4, 4)}
            },
            'D': {0: (2, 43, 43)}
        }
    },
    'T': {
        0: (3, 3, 3),
        'C': {
            0: (4, 4, 4),
            'H': {0: (4, 4, 4)}
        },
        'Z': {
            0: (4, 4, 4),
            'S': {0: (4, 4, 4)}
        },
        'S': {
            0: (4, 4, 4),
            'Z': {0: (4, 4, 4)},
            'H': {0: (4, 4, 4)},
            'C': {
                'H': {0: (4, 4, 4)}
            }
        },
        'T': {
            'S': {
                0: (4, 4, 4),
                'Z': {0: (4, 4, 4)},
                'C': {
                    'H': {0: (4, 4, 4)}
                }
            },
            'C': {
                'H': {0: (4, 4, 4)}
            },
            'Z': {0: (4, 4, 4)}
        },
        'H': {0: (3, 3, 3)},
        'R': {
            'Z': {0: (4, 4, 4)},
            'S': {0: (4, 4, 4)}
        }
    },
    'U': {
        0: (0, -1, -1),
        'E': {0: (0, -1, -1)},
        'I': {0: (0, 1, -1)},
        'J': {0: (0, 1, -1)},
        'Y': {0: (0, 1, -1)}
    },
    'V': {0: (7, 7, 7)},
    'W': {0: (7, 7, 7)},
    'X': {0: (5, 54, 54)},
    'Y': {0: (1, -1, -1)},
    'Z': {
        0: (4, 4, 4),
        'D': {
            0: (2, 43, 43),
            'Z': {
                0: (2, 4, 4),
                'H': {0: (2, 4, 4)}
            }
        },
        'H': {
            0: (4, 4, 4),
            'D': {
                0: (2, 43, 43),
                'Z': {
                    'H': {0: (2, 4, 4)}
                }
            }
        },
        'S': {
            0: (4, 4, 4),
            'H': {0: (4, 4, 4)},
            'C': {
                'H': {0: (4, 4, 4)}
            }
        }
    }
}


translit = {
    'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g',
    'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
    'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'J', 'й': 'j', 'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'P', 'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't',
    'У': 'Y', 'у': 'y', 'Ф': 'F', 'ф': 'f', 'Х': 'H', 'х': 'h', 'Ц': 'C', 'ц': 'c',
    'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Sch', 'щ': 'sch', 'Ъ': '\'', 'ъ': '\'',
    'Ы': 'Y', 'ы': 'y', 'Ь': '\'', 'ь': '\'', 'Э': 'E', 'э': 'e', 'Ю': 'Ju', 'ю': 'ju',
    'Я': 'Ja', 'я': 'ja'
}


translit_map = str.maketrans(translit)


def prepare_string(s):
    return re.sub(r'\s+', ' ', re.sub(r'\b[^\s]{1,3}\b', '', re.sub(r'[^\w\s]|\d', '', s.strip().upper())))


def cyr_translit(s):
    return s.translate(translit_map)


def replace_table(s, t_from, t_to):
    for f, t in zip(t_from, t_to):
        s = re.sub(f, t, s)
    return s


def phonetic_split(s, alg):
    if re.search(r'[А-Яа-я]', s):
        is_cyrillic = True
        s = s.translate(translit_map)
    else:
        is_cyrillic = False
    s = prepare_string(s)
    if not s:
        return None
    tokens = s.split()
    matches = {}
    for token in tokens:
        matches[token] = alg(token, is_cyrillic)
    return matches


def phonetic(s, alg, prepare=True):
    if re.search(r'[А-Яа-я]', s):
        is_cyrillic = True
        s = s.translate(translit_map)
    else:
        is_cyrillic = False
    if prepare:
        s = prepare_string(s)
    if not s:
        return None
    return alg(s, is_cyrillic)


def daitch_mokotoff(s, is_cyrillic=False):
    s = s.upper()
    length = len(s)
    output = ''
    i = 0
    previous = -1
    while i < length:
        current = last = codes[s[i]]
        j = k = 1
        while k < 7:
            if i + k >= length or s[i + k] not in current:
                break
            current = current[s[i + k]]
            if 0 in current:
                last = current
                j = k + 1
            k += 1
        if i == 0:
            code = last[0][0]
        elif i + j >= length or codes[s[i + j]][0][0] != 0:
            code = (last[1][2] if 1 in last else last[0][2]) if is_cyrillic else last[0][2]
        else:
            code = (last[1][1] if 1 in last else last[0][1]) if is_cyrillic else last[0][1]
        if code != -1 and code != previous:
            output += str(code)
        previous = code
        i += j
    return output[0:6].ljust(6, '0')


def caverphone(s, *args):
    s = s.casefold()
    s = re.sub(r'e+$', '', s)
    s = replace_table(s, ['^cough', '^rough',	'^tough', '^enough', '^gn', '^mb'],
                         ['cou2f', 'rou2f', 'tou2f', 'enou2f', '2n', 'm2'])
    s = replace_table(s,
                      ['cq', 'ci', 'ce', 'cy', 'tch', 'c', 'q', 'x', 'v', 'dg', 'tio',
                       'tia', 'd', 'ph', 'b', 'sh', 'z'],
                      ['2q', 'si', 'se', 'sy', '2ch', 'k', 'k', 'k', 'f', '2g', 'sio',
                       'sia', 't', 'fh', 'p', 's2', 's']
                      )
    s = re.sub(r'^[aeiou]', 'A', s)
    s = re.sub(r'[aeiou]', '3', s)

    s = replace_table(s, ['j', '^y3', '^y', 'y', '3gh3', 'gh', 'g', 's+', 't+', 'p+', 'k+', 'f+', 'm+'],
                      ['y', 'Y3', 'A', '3', '3kh3', '22', 'k', 'S', 'T', 'P', 'K', 'F', 'M'])
    s = replace_table(s, ['n+', 'w3', 'wh3', 'w$', 'w', '^h', 'h', 'r3', 'r$', 'r', 'l3', 'l$', 'l'],
                      ['N', 'W3', 'Wh3', '3', '2', 'A', '2', 'R3', '3', '2', 'L3', '3', '2'])
    s = s.replace('2', '')
    s = re.sub(r'3$', 'A', s)
    s = s.replace('3', '')
    return s[0:10].ljust(10, '1')