import numpy as np
import cv2

cap = cv2.VideoCapture("https://video-weaver.fra02.hls.ttvnw.net/v1/playlist/CtEDo9zkLJnpzh9_WUgGJF9zdxuvFp3c5I1WbOYzGn_qM5unnc0hXTkBlh-4hfBPCIPODlIlA7pokztqX7j_5tYRiMVi8uw2k-Bc88-F7BIsIuLU2A4wNVVSPSlX4DZUjDmOpX81EHytraWcL9kzktpgeniaF73qL5qFYH-_p2mrb5rhgjnpVYZJ8djvcUZvezDUlx43U1bNN--iorUwEUDFJBW35RGkOQ--SUgTgYiY3EBM7-ng1C4YmLb_seY3VrhNYn_FvzyW69Z-ZipyXUmEal3AhMeNhCRLG_KDUitG_-lNqB4i9OWPj7f3YVw6Y6evwn9UwIk3_Sb92ByLhLXH5flBCaiFZ7Zdcp_7mZL5g0prLl-OKn4vHccZh0T78Do1QFJAygcz3aPUiOAbBWgYnW7VR7AM09kX3Wk4tAwWofWGfHh2L0l2LiUF1OQyLmmF5wEKJRPxd7IjZGpe-cUtbEKDq_QUngw-GCMh7tbmjAv85U4j8bQuf05THmO2cR6yV4PvasRPnBzfctA7xLweWEEQvU3i0a_AcOFZRPMH9raCYnEzvYAs0H962YIB1QQbfby23uJZkmvrGoVcDSfygHXDbeVaP0PB2BaAWCT6OBGDEhAx_BnbY5lYMRYxiV44__HDGgx36lqmKAO__iKC2gQ.m3u8")

while(True):

    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()