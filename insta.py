from instagrapi import Client
cl = Client()
cl.login("shrinath3113", "31131997")

user_id = cl.user_id_from_username("arshinasumbul")
medias = cl.user_medias(user_id)
i=0
for m in medias:
    #print(i,m)
    if(i>=1):
        break
    if m.media_type == 1:
            # Photo
            cl.photo_download(m.pk)
            i+=1

print("done")