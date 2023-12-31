from instagrapi import Client
from PIL import Image
import time
import random

cl = Client()
#cl.login("techshirtofficial", "Tech-shirtinstagram")
cl.login("linkeando365","instagramdelikes")
#cl.login("javiichuu","Instagram2005")

"""media = cl.photo_upload(
    path="C:\\Users\\javit\\Escritorio\\programacion\\bot\\BANK-TECH-Digital-2251407135.JPEG",
    caption="Tech-shirt #tech"
)"""

"""hashtag="programming"
print("Esto funciona 3")
medias=cl.hashtag_medias_recent("programming", amount=20)
print("Esto funciona 4")

for i, media in enumerate(medias):
    cl.media_like(media.id)
    print(f"Liked post number {i+1} of hastag {hashtag}")

    cl.user_follow(media.user.pk)
    print(f"Followed user {media.user.username}")

    cl.media_comment(media.id, "Something")"""
username=[]
coments=cl.media_comments(media_id="3261991640663472746_2103053595", amount=20)
userid=cl.user_id_from_username(username="infocomputer_")
users=cl.user_followers(user_id=userid, amount=20)
for user in users:
    username.append(cl.username_from_user_id(user_id=user))
    with open()
    #media=cl.media_comment(media_id="3261991640663472746_2103053595",text=username)
#for coment in coments:
#    print(coment.user.username)
#media=cl.media_comment(media_id="3261991640663472746_2103053595",text="@techshirtofficial @linkeando365 ")

"""user_id = cl.user_id_from_username("infocomputer_")
medias = cl.user_medias(user_id, 20)
for media in medias:
    print(media.id)"""