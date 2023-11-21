import requests as r


url = 'https://jsonplaceholder.typicode.com/posts'
url2 = 'https://jsonplaceholder.typicode.com/comments'
posts_list = r.get(url).json()
comment_list = r.get(url2).json()
com_count = 0
for comment in comment_list:
    if comment['postId'] == 5:
        com_count += 1
print(f' к посту №5 оставили {com_count} комментариев')
    

social_media = {}
for post in posts_list:
    social_media [post['id']] = {"title": post["title"], "body": post["body"], "comments": []}
for comment in comment_list:
    post = social_media[comment['postId']]['comments']
    comm = {"id": comment["id"],
    "title": comment["name"],
    "body": comment["body"]}
    post.append(comm)

for post in social_media:
    print(f'Post id: {post}\n Post title: {social_media[post]["title"]}')
    print(f'Post body: {social_media[post]["body"]}')
    print('\nComments:')
    for comment in social_media[post]["comments"]:
        print(f'\t\tHeading: {comment["title"]}\n\t\tText:{comment["body"]}')