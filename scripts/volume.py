from subprocess import call
valid = False

while not valid:
    volume = input('What volume? > ')

    try:
        volume = int(volume)

        if (volume <= 100) and (volume >= 0):
            call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
            valid = True

    except ValueError:
        pass
