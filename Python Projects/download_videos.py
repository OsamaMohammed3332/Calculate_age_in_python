from pafy import new

while True:
    try:
        link = input("enter your link:")
        video = new(link)
        choice3 = input("video(1) or audio(2):")
        if choice3 == "1":
            def vd():
                stream = video.streams
                n = 1
                for q in stream:
                    print("(", n, ")", q)
                    n += 1
                choice1 = int(input("enter your choice:"))

                if choice1 == 1:
                    stream[0].download()
                elif choice1 == 2:
                    stream[1].download()

                else:
                    print("wrong number")


            vd()
        elif choice3 == "2":
            def ad():
                au_stream = video.audiostreams
                n1 = 1
                for a in au_stream:
                    print("(", n1, ")", a)
                    n1 += 1
                choice2 = int(input("enter your choice:"))

                if choice2 == 1:
                    au_stream[0].download()
                elif choice2 == 2:
                    au_stream[1].download()
                elif choice2 == 3:
                    au_stream[2].download()
                elif choice2 == 4:
                    au_stream[3].download()

                else:
                    print("wrong number")


            ad()

        else:
            print("wrong choice")

    except:
        print("Value error")
