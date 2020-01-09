from string import Template

import panflute as pf

metafields = ['title', 'alt_title', 'dish', 'temp', 'time', 'source', 'size', 'tags']


def title(doc):
    m = {x: '' for x in metafields}
    m.update(doc.get_metadata())
    t = Template(r'\begin{recipe}[$alt_title]{$title}{$dish \hfill $temp \hfill $time}{\textbf{Source:} $source \hfill serves $size}')

    return t.safe_substitute(m)

# def steps(elem, doc):
#     if isinstance(elem, )
#     return
#
# def cleanup(elem, doc):
#     if


def rmd2tex(doc):
    title = title(doc)
    recipe = title + r'\n\end{recipe}'

    return recipe


def main(doc=None):
    return pf.run_filter(steps, title, rmd2tex, doc=doc)


if __name__ == '__main__':
    main()
