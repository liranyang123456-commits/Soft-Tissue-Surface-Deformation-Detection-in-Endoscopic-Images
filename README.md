# iScience-soft tissue Tracking Experiments

This repository contains the final, reproducible implementation and results for the chessboard-based tracking evaluation in the iScience manuscript.

## Contents

- `code/` — Core tracking implementation (ContourSimilarityNet + HistAB + NanoTrack)
- `results/` — Aggregated metrics and per-sequence results
- `docs/` — LaTeX table fragments and supplementary material

## Key Numbers (Coverage-Aware IoU)

| Method | IoU (mean ± SD) | Success | Precision | CtrErr |
|--------|-----------------|---------|-----------|--------|
| Ours (Scheme C + NanoTrack) | 0.809 ± 0.211 | 0.888 | 0.648 | 70.8 |
| MixFormer | 0.540 ± 0.114 | 0.440 | 0.019 | 217.6 |
| LMTrack | 0.536 ± 0.176 | 0.444 | 0.017 | 219.1 |
| OSTrack | 0.523 ± 0.130 | 0.425 | 0.014 | 225.9 |
| CSRT | 0.356 ± 0.334 | 0.291 | 0.129 | 231.5 |
| SAM | 0.333 ± 0.275 | 0.323 | 0.226 | 341.4 |
| YOLO-seg | 0.305 ± 0.165 | 0.301 | 0.091 | 544.0 |
| Cutie | 0.288 ± 0.223 | 0.219 | 0.049 | 237.0 |

All metrics use the coverage-aware BBox IoU (prediction fully covering GT → 1.0).

## Reproducibility

### Reproduce the metrics (Table 6) from bundled data — self-contained
```bash
pip install -r requirements.txt        # numpy, scipy
python reproduce.py
```
This recomputes the coverage-aware BBox IoU (mean ± SD) and the Wilcoxon
significance for our method and all baselines, directly from the bundled
per-frame result CSVs in `results/`. Expected output is in
`docs/reproduce_output.txt`; the LaTeX table is in `docs/tracking_table.tex`.

Bundled data (all paths repository-relative):
- `results/Final_Optimize_v3/` — Ours (ours_scheme_c_nano) and NanoTrack per-frame
  ground-truth/prediction boxes (11 sequences, 3,848 frames).
- `results/Baselines_iScience_GTMask/` — per-frame boxes for CSRT, SAM, YOLO-seg,
  OSTrack, MixFormer, LMTrack, Cutie under the same coverage-aware protocol.

### Run the tracker end-to-end (raw video → predictions)
This additionally requires model weights and the raw chessboard dataset, which are
large and provided separately (see below):
- ContourSimilarityNet weights (`contour_similarity_best.pt`)
- NanoTrack ONNX (`nanotrack_backbone_sim.onnx`, `nanotrack_head_sim.onnx`)
- Chessboard sequences + ground-truth masks

Core code: `code/HistAB_core.py` (tracker), `code/train_contour_similarity.py`
(similarity network), `code/compare_iscience_tracking.py` (evaluation).
Set the model/data locations via the environment variables documented at the top
of `HistAB_core.py` (e.g., `MIS_CONTOUR_SIM_CKPT`).

## Model weights & dataset availability
Model checkpoints and the raw chessboard dataset are available from the lead
contact upon reasonable request / via the release attached to this repository
(too large to host in the source tree).

## Citation

If you use this code or data, please cite the corresponding iScience paper (to be updated upon acceptance).

## License

Code is released under the MIT License (see LICENSE). Data files retain their original licenses.
