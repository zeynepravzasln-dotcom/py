import cv2
import numpy as np

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Aynalama (doğal görünüm için)
    frame = cv2.flip(frame, 1)

    # Görüntü boyutu
    h, w, _ = frame.shape
    cx, cy = w // 2, h // 2

    # Bölge çizgileri
    cv2.line(frame, (cx, 0), (cx, h), (200, 200, 200), 2)
    cv2.line(frame, (0, cy), (w, cy), (200, 200, 200), 2)

    # Bölge isimleri
    cv2.putText(frame, "A", (cx//2 - 20, cy//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, "B", (cx + cx//2 - 20, cy//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, "C", (cx//2 - 20, cy + cy//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, "D", (cx + cx//2 - 20, cy + cy//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # HSV dönüşümü
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi renk aralığı
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    # Maskeyi oluştur
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Gürültü azaltma
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

    # Konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # En büyük kontur
        c = max(contours, key=cv2.contourArea)
        (x, y, w_box, h_box) = cv2.boundingRect(c)

        # Konturun merkezini bul
        obj_cx = x + w_box // 2
        obj_cy = y + h_box // 2

        # Görselleştir
        cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
        cv2.circle(frame, (obj_cx, obj_cy), 5, (0, 0, 255), -1)

        # Bölge tespiti
        if obj_cx < cx and obj_cy < cy:
            region = "A"
        elif obj_cx > cx and obj_cy < cy:
            region = "B"
        elif obj_cx < cx and obj_cy > cy:
            region = "C"
        else:
            region = "D"

        # Bölge bilgisini ekrana yaz
        cv2.putText(frame, f"Nesne {region} bolgesinde", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Mavi Nesne Takip Sistemi", frame)
    cv2.imshow("Maske", mask)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC tuşu
        break

cap.release()
cv2.destroyAllWindows()