def hisobla(matnlar):
    natijalar = []
    for matn in matnlar:
        punktatsiya_soni = sum(1 for belgi in matn if not belgi.isalnum() and not belgi.isspace())
        tozalangan_matn = ''.join([belgi for belgi in matn if belgi.isalnum() or belgi.isspace()])
        natijalar.append((punktatsiya_soni, tozalangan_matn))
    return natijalar

matnlar = ["Salom, dunyo!", "Python dasturlash tili juda qulay.", "Bu bir misol matn."]
print(hisobla(matnlar))
