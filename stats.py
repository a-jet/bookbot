    
def get_word_count(content):
    words = content.split()
    return len(words)


def get_char_count(content):
    out={}
    content = content.lower()
    for char in content:
        if char in out:
            out[char]=out[char]+1
        else:
            out[char]=1
    return out



def get_sort_on(dict):
    return dict["count"]


def get_sorted_char_count(content):
    f_out = get_char_count(content)
    s_out=[]
    for key in f_out:
        t_out={}
        t_out["char"] = key
        t_out["count"] = f_out[key]
        s_out.append(t_out)
    s_out.sort(reverse=True, key=get_sort_on)

    return s_out