#!/usr/bin/env python3
"""Download media assets from PolyU IPNL website into Hugo static/images/."""

import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
STATIC_IMAGES = os.path.join(PROJECT_ROOT, "static", "images")

IMG_BASE = "https://www.polyu.edu.hk/aae/ipn-lab/img/"
SEM_BASE = "https://www.polyu.edu.hk/aae/ipn-lab/us/activities%20%26%20events/sem/"
MC_BASE = "https://www.polyu.edu.hk/aae/ipn-lab/us/activities%20%26%20events/mc/"
STD_BASE = "https://www.polyu.edu.hk/aae/ipn-lab/us/activities%20%26%20events/std/"

HEADERS = {"User-Agent": "IPNL-Hugo-Migration/1.0 (lt.hsu@polyu.edu.hk)"}

# Each entry: (base_url, remote_filename, local_subdir, local_filename)
DOWNLOADS = [
    # ===== LOGOS =====
    (IMG_BASE, "l/IPNL_logo.png", "logos", "ipnl-logo.png"),
    (IMG_BASE, "l/aaelogo.png", "logos", "aaelogo.png"),

    # ===== BANNERS =====
    (IMG_BASE, "l/home_banner_1.png", "banners", "home-banner-1.png"),
    (IMG_BASE, "l/home_banner_4.png", "banners", "home-banner-4.png"),
    (IMG_BASE, "l/home_banner_6.png", "banners", "home-banner-6.png"),
    (IMG_BASE, "l/home_banner_7.png", "banners", "home-banner-7.png"),
    (IMG_BASE, "l/page_banner_aboutus.png", "banners", "page-banner-aboutus.png"),
    (IMG_BASE, "l/page_banner_ne.png", "banners", "page-banner-news.png"),
    (IMG_BASE, "l/page_banner_projects.png", "banners", "page-banner-projects.png"),

    # ===== TEAM PHOTOS =====
    # PI already exists as static/images/li-ta-hsu-2022.jpg — skip
    (IMG_BASE, "aboutus/xiwei.JPG", "people", "xiwei-bai.jpg"),
    (IMG_BASE, "aboutus/shiyu.jpg", "people", "shiyu-bai.jpg"),
    (IMG_BASE, "aboutus/huangfeng.png", "people", "feng-huang.png"),
    (IMG_BASE, "aboutus/haosheng.png", "people", "haosheng-xu.png"),
    (IMG_BASE, "aboutus/hoifung.png", "people", "hoi-fung-ng.png"),
    (IMG_BASE, "aboutus/penghui.png", "people", "penghui-xu.png"),
    (IMG_BASE, "aboutus/maxlee.png", "people", "max-lee.png"),
    (IMG_BASE, "aboutus/jiachong.png", "people", "jiachong-chang.png"),
    (IMG_BASE, "aboutus/penggao.jpg", "people", "penggao-yan.jpg"),
    (IMG_BASE, "aboutus/xiaxiao.jpg", "people", "xiao-xia.jpg"),
    (IMG_BASE, "aboutus/hongmin.jpg", "people", "hongmin-zhang.jpg"),
    (IMG_BASE, "aboutus/SONG%20Baoshan.jpg", "people", "baoshan-song.jpg"),
    (IMG_BASE, "aboutus/meiling.jpg", "people", "meiling-su.jpg"),
    (IMG_BASE, "aboutus/LI%20Yuan.jpg", "people", "yuan-li.jpg"),
    (IMG_BASE, "aboutus/auston.png", "people", "chin-lok-tsang.png"),
    (IMG_BASE, "aboutus/gulu.jpg", "people", "gulu-lab-cat.jpg"),

    # ===== HOMEPAGE EVENT THUMBNAILS =====
    (IMG_BASE, "l/20230320.jpg", "news", "thumb-20230320.jpg"),
    (IMG_BASE, "l/20221026.jpg", "news", "thumb-20221026.jpg"),
    (IMG_BASE, "l/20220901.jpg", "news", "thumb-20220901.jpg"),
    (IMG_BASE, "l/20220831.jpg", "news", "thumb-20220831.jpg"),
    (IMG_BASE, "l/20220322.jpg", "news", "thumb-20220322.jpg"),
    (IMG_BASE, "l/20211130.jpg", "news", "thumb-20211130.jpg"),
    (IMG_BASE, "l/20191206.jpg", "news", "thumb-20191206.jpg"),
    (IMG_BASE, "l/20190916.jpg", "news", "thumb-20190916.jpg"),
    (IMG_BASE, "l/20190721.jpg", "news", "thumb-20190721.jpg"),
    (IMG_BASE, "l/20190710.png", "news", "thumb-20190710.png"),
    (IMG_BASE, "l/20190101.jpg", "news", "thumb-20190101.jpg"),
    (IMG_BASE, "l/20181202.jpg", "news", "thumb-20181202.jpg"),
    (IMG_BASE, "l/20180926.jpg", "news", "thumb-20180926.jpg"),
    (IMG_BASE, "l/20171113.jpg", "news", "thumb-20171113.jpg"),

    # ===== SEMINAR & EVENT PHOTOS =====
    # IEEE ITSC 2023 Workshop (Sep 2023)
    (SEM_BASE, "20230930a.png", "news", "20230930a.png"),
    (SEM_BASE, "20230930b.png", "news", "20230930b.png"),
    (SEM_BASE, "20230930c.png", "news", "20230930c.png"),
    (SEM_BASE, "20230930d.png", "news", "20230930d.png"),
    (SEM_BASE, "20230930e.png", "news", "20230930e.png"),
    (SEM_BASE, "20230930f.png", "news", "20230930f.png"),
    # Dr. Chaochung Peng Visit (Jul 2023)
    (SEM_BASE, "20230713a.jpg", "news", "20230713a.jpg"),
    (SEM_BASE, "20230713b.jpg", "news", "20230713b.jpg"),
    # Dr. Guoquan Huang Visit (Jun 2023)
    (SEM_BASE, "20230621a.jpg", "news", "20230621a.jpg"),
    (SEM_BASE, "20230621b.jpg", "news", "20230621b.jpg"),
    # GNSS Seminar (Mar 2023)
    (SEM_BASE, "20230320a.jpg", "news", "20230320a.jpg"),
    (SEM_BASE, "20230320b.png", "news", "20230320b.png"),
    # SAIC Meeting (Nov 2022)
    (SEM_BASE, "20221104a.png", "news", "20221104a.png"),
    (SEM_BASE, "20221104b.png", "news", "20221104b.png"),
    (SEM_BASE, "20221104c.png", "news", "20221104c.png"),
    # ASTRI Lab Visit (Oct 2022)
    (SEM_BASE, "20221026a.jpg", "news", "20221026a.jpg"),
    (SEM_BASE, "20221026b.jpg", "news", "20221026b.jpg"),
    # Certificate Awards (Aug 2022)
    (SEM_BASE, "20220901a.jpg", "news", "20220901a.jpg"),
    (SEM_BASE, "20220901b.jpg", "news", "20220901b.jpg"),
    (SEM_BASE, "20220901c.jpg", "news", "20220901c.jpg"),
    (SEM_BASE, "20220901d.jpg", "news", "20220901d.jpg"),
    (SEM_BASE, "20220901e.jpg", "news", "20220901e.jpg"),
    (SEM_BASE, "20220901f.jpg", "news", "20220901f.jpg"),
    (SEM_BASE, "20220901g.jpg", "news", "20220901g.jpg"),
    (SEM_BASE, "20220901h.jpg", "news", "20220901h.jpg"),
    (SEM_BASE, "20220901i.jpg", "news", "20220901i.jpg"),
    # Endowed Young Scholars (Aug 2022)
    (SEM_BASE, "20220831a.jpg", "news", "20220831a.jpg"),
    (SEM_BASE, "20220831b.jpg", "news", "20220831b.jpg"),
    (SEM_BASE, "20220831c.jpg", "news", "20220831c.jpg"),
    # Cheung Chau Gathering (Mar 2022)
    (SEM_BASE, "20220322a.jpg", "news", "20220322a.jpg"),
    (SEM_BASE, "20220322b.jpg", "news", "20220322b.jpg"),
    (SEM_BASE, "20220322c.jpg", "news", "20220322c.jpg"),
    (SEM_BASE, "20220322d.jpg", "news", "20220322d.jpg"),
    (SEM_BASE, "20220322e.jpg", "news", "20220322e.jpg"),
    # Halloween Party (Nov 2021)
    (SEM_BASE, "20221130a.jpg", "news", "20211130a.jpg"),
    # UrbanLoco Dataset (Mar & May 2020)
    (SEM_BASE, "20200330a.png", "news", "20200330a.png"),
    (SEM_BASE, "20200330b.png", "news", "20200330b.png"),
    (SEM_BASE, "20200330c.png", "news", "20200330c.png"),
    (SEM_BASE, "20200520a.png", "news", "20200520a.png"),
    # Qianhai Competition (Dec 2019)
    (SEM_BASE, "20191206a.jpg", "news", "20191206a.jpg"),
    (SEM_BASE, "20191206b.jpg", "news", "20191206b.jpg"),
    (SEM_BASE, "20191206c.jpg", "news", "20191206c.jpg"),
    # ION GNSS+ 2019 (Sep 2019)
    (SEM_BASE, "20190916a.jpg", "news", "20190916a.jpg"),
    (SEM_BASE, "20190916b.png", "news", "20190916b.png"),
    (SEM_BASE, "20190916c.jpg", "news", "20190916c.jpg"),
    (SEM_BASE, "20190916d.png", "news", "20190916d.png"),
    (SEM_BASE, "20190916e.jpg", "news", "20190916e.jpg"),
    # IPNL Retreat (Jul 2019)
    (SEM_BASE, "20190721a.jpg", "news", "20190721a.jpg"),
    (SEM_BASE, "20190721b.jpg", "news", "20190721b.jpg"),
    (SEM_BASE, "20190721c.jpg", "news", "20190721c.jpg"),
    (SEM_BASE, "20190721d.jpg", "news", "20190721d.jpg"),
    (SEM_BASE, "20190721e.jpg", "news", "20190721e.jpg"),
    (SEM_BASE, "20190721f.jpg", "news", "20190721f.jpg"),
    (SEM_BASE, "20190721g.jpg", "news", "20190721g.jpg"),
    (SEM_BASE, "20190721h.jpg", "news", "20190721h.jpg"),
    # Dr. Taro Suzuki Visit (Jul 2019)
    (SEM_BASE, "20190710a.png", "news", "20190710a.png"),
    # 8th Asia MAE Workshop (Dec 2018)
    (SEM_BASE, "20181202a.jpg", "news", "20181202a.jpg"),
    (SEM_BASE, "20181202b.jpg", "news", "20181202b.jpg"),
    (SEM_BASE, "20181202c.jpg", "news", "20181202c.jpg"),
    (SEM_BASE, "20181202d.jpg", "news", "20181202d.jpg"),
    # ION GNSS+ 2018 (Sep 2018)
    (SEM_BASE, "20180926a.jpg", "news", "20180926a.jpg"),
    # GNSS Summer School (Jul 2018)
    (SEM_BASE, "20180730a.png", "news", "20180730a.png"),
    # Songshan Lake Competition (Jan 2018)
    (SEM_BASE, "20180112a.jpg", "news", "20180112a.jpg"),
    (SEM_BASE, "20180112b.jpg", "news", "20180112b.jpg"),
    # ICASE Keynote (Nov 2017)
    (SEM_BASE, "20171113a.jpg", "news", "20171113a.jpg"),
    (SEM_BASE, "20171113b.jpg", "news", "20171113b.jpg"),
    (SEM_BASE, "20171113c.jpg", "news", "20171113c.jpg"),
    # GNSS Summer School (Jul 2017)
    (SEM_BASE, "20170730a.png", "news", "20170730a.png"),

    # ===== STUDENT ACTIVITY PHOTOS =====
    (STD_BASE, "20221006a.jpg", "news", "std-20221006a.jpg"),
    (STD_BASE, "20221006b.jpg", "news", "std-20221006b.jpg"),
    (STD_BASE, "20221006c.jpg", "news", "std-20221006c.jpg"),
    (STD_BASE, "20221006d.jpg", "news", "std-20221006d.jpg"),
    (STD_BASE, "20220730a.jpg", "news", "std-20220730a.jpg"),
    (STD_BASE, "20220730b.jpg", "news", "std-20220730b.jpg"),
    (STD_BASE, "20220730c.jpg", "news", "std-20220730c.jpg"),

    # ===== MEDIA COVERAGE IMAGES =====
    (MC_BASE, "mc20230104.png", "news/media", "mc20230104.png"),
    (MC_BASE, "mc20221110.png", "news/media", "mc20221110.png"),
    (MC_BASE, "mc20221012.png", "news/media", "mc20221012.png"),
    (MC_BASE, "mc20221003a.png", "news/media", "mc20221003a.png"),
    (MC_BASE, "mc20221003b.png", "news/media", "mc20221003b.png"),
    (MC_BASE, "mc20221003c.png", "news/media", "mc20221003c.png"),
    (MC_BASE, "mc20220805.png", "news/media", "mc20220805.png"),
    (MC_BASE, "mc20220709.png", "news/media", "mc20220709.png"),
    (MC_BASE, "mc20220708.png", "news/media", "mc20220708.png"),
    (MC_BASE, "mc20220403.png", "news/media", "mc20220403.png"),
]


def download_file(url, dest_path):
    """Download a file, return True on success."""
    if os.path.exists(dest_path):
        return "skip"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as f:
            f.write(data)
        size_kb = len(data) / 1024
        return f"ok ({size_kb:.0f} KB)"
    except urllib.error.HTTPError as e:
        return f"HTTP {e.code}"
    except Exception as e:
        return f"error: {e}"


def main():
    ok_count = 0
    skip_count = 0
    fail_count = 0
    failures = []

    total = len(DOWNLOADS)
    print(f"Downloading {total} files...\n")

    for i, (base_url, remote_file, local_subdir, local_file) in enumerate(DOWNLOADS, 1):
        url = base_url + remote_file
        dest = os.path.join(STATIC_IMAGES, local_subdir, local_file)

        result = download_file(url, dest)
        status_char = "." if result.startswith("ok") else ("S" if result == "skip" else "X")

        if result.startswith("ok"):
            ok_count += 1
        elif result == "skip":
            skip_count += 1
        else:
            fail_count += 1
            failures.append((local_file, result))

        print(f"  [{i:3d}/{total}] {status_char} {local_subdir}/{local_file} — {result}")
        if result != "skip":
            time.sleep(0.5)

    print(f"\n{'='*50}")
    print(f"Done: {ok_count} downloaded, {skip_count} skipped, {fail_count} failed")
    if failures:
        print(f"\nFailed downloads:")
        for name, reason in failures:
            print(f"  - {name}: {reason}")


if __name__ == "__main__":
    main()
