# Harris Corner Detector – INF605 Group 15

Final project for INF605 Fundamentals of Image Processing.
We study and implement the corner detector from:

> C. Harris and M. Stephens, "A combined corner and edge detector," in *Proc. 4th Alvey Vision Conference*, Manchester, U.K., 1988, pp. 147–151, doi: 10.5244/C.2.23.
> [Paper (PDF)](https://bmva-archive.org.uk/bmvc/1988/avc-88-023.pdf)

## Team

| # | Name | GitHub |
|---|------|--------|
| 1 | Eren Şimşek (contact) | [@erensmsek](https://github.com/erensmsek) |
| 2 | Mert Oğuz Mirzaoğlu | [@mertmrz](https://github.com/mertmrz) |
| 3 | Muhammet Şimşek | [@muhametsmsek](https://github.com/muhametsmsek) |
| 4 | Ahmetcan Karabulut | [@ackrbulut11](https://github.com/ackrbulut11) |
| 5 | Yunus Emre Erdoğan | [@Yunus1942](https://github.com/Yunus1942) |

## What we implement

- Image gradients with our own Sobel kernels
- Structure tensor (second moment matrix) with a Gaussian window
- Corner response `R = det(M) - k * trace(M)^2`
- Thresholding and non-maximum suppression
- Corner matching between two views of the same scene
- Repeatability under rotation and brightness change
- Comparison with `cv2.cornerHarris` (used for comparison only)

## Repository layout

```
harris_corner_detector.ipynb   main notebook
data/                          test images
results/                       saved figures
slides/                        presentation (PDF)
report/                        final report (PDF)
exercises/                     weekly course exercise scripts
progress.md                    progress tracking (done / to do)
requirements.txt
```

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook harris_corner_detector.ipynb
```

Run all cells from top to bottom.

## AI usage

AI tools were used for assistance during this project. The full disclosure is given in the final report.
