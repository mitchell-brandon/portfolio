# phase1: refactor this code into a main() function
#phase2: write a forloop that loops through the list/dict and executes the templating
def main():
    print('building ssg')
    pages = [{
        'filename': 'contents/index.html',
        'output': 'docs/index.html',
        'title': 'About',
    },
    {
        'filename': 'contents/blog.html',
        'output': 'docs/blog.html',
        'title': 'Blog',
    },
    {
        'filename': 'contents/contact.html',
        'output': 'docs/contact.html',
        'title': 'Contact',
    }]
    # variables that read top and bottom html
    top_html = open('templates/top.html').read()
    bottom_html = open('templates/bottom.html').read()

    for page in pages:
        title = page['title']
        filename = page['filename']
        output = page['output']

        if filename == 'contents/index.html' and title == 'About' and output == 'docs/index.html':

            print('filename =', filename, 'title =', title, 'output =', output)
            mid_index_html = open(filename).read()
            index_html = top_html + mid_index_html + bottom_html
            # open('docs/index.html', 'w+').write(output)
            open(output, 'w+').write(index_html)

        elif filename == 'contents/blog.html' and title == 'Blog' and output == 'docs/blog.html':

            print('filename =', filename, 'title =', title, 'output =', output)
            mid_blog_html = open(filename).read()
            blog_html = top_html + mid_blog_html + bottom_html
            # open('docs/blog.html', 'w+').write(output)
            open(output, 'w+').write(blog_html)

        elif filename == 'contents/contact.html' and title == 'Contact' and output == 'docs/contact.html':

            print('filename =', filename, 'title =', title, 'output =', output)
            mid_contact_html = open(filename).read()
            contact_html = top_html + mid_contact_html + bottom_html
            # open('docs/contact.html', 'w+').write(output)
            open(output, 'w+').write(contact_html)
        else: pass

main()




# variables that read top and bottom html
    # top_html = open('templates/top.html').read()
    # bottom_html = open('templates/bottom.html').read()

#variables that read the middle contents of html
    # mid_index_html = open('contents/index.html').read()
    # mid_blog_html = open('contents/blog.html').read()
    # mid_contact_html = open('contents/contact.html').read()    

# combining tops + html middle contents + bottoms
    # index_html = top_html + mid_index_html + bottom_html
    # blog_html = top_html + mid_blog_html + bottom_html
    # contact_html = top_html + mid_contact_html + bottom_html

#writing/creating the new html pages: stored in html directory, this is the output
    # open('docs/index.html', 'w+').write(index_html)
    # open('docs/blog.html', 'w+').write(blog_html)
    # open('docs/contact.html', 'w+').write(contact_html)



