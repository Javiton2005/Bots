from instagrapi import Client
import time
import random

cl = Client()
cl.login("techshirtofficial", "Tech-shirtinstagram")
#cl.login("linkeando365","instagramdelikes")

"""media = cl.photo_upload(
    path="C:\\Users\\javit\\Escritorio\\programacion\\bot\\BANK-TECH-Digital-2251407135.JPEG",
    caption="Tech-shirt #tech"
)"""

hashtag="programming"
print("Esto funciona 3")
medias=cl.hashtag_medias_recent("programming", amount=20)
print("Esto funciona 4")

for i, media in enumerate(medias):
    cl.media_like(media.id)
    print(f"Liked post number {i+1} of hastag {hashtag}")

    cl.user_follow(media.user.pk)
    print(f"Followed user {media.user.username}")

    cl.media_comment(media.id, "Something")