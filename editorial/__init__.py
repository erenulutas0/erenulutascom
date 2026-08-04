"""Elle yazılmış sayılar.

Her `ed_YYYY_MM_DD.py` dosyası bir günün içeriğini tutar. `apply.py` hepsini
tarayıp `content/` altına JSON olarak yazar.

Otomatik pipeline (`python -m pipeline.cli daily`) devreye girdiğinde bu klasör
arşivin kaynağı olarak kalır — yeni günler doğrudan content/ altına üretilir.
"""
