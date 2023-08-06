## Analyzing MiniSEED seismic data in MATLAB 

For details on the usage, visit the earthinversion post: https://www.earthinversion.com/utilities/converting-mseed-data-to-mat-and-analyzing-in-matlab/

## Output data structure

- `stats` contains all the meta data information corresponding to each trace, and
- `data` contain the time series data

```
mat_file.mat -> stats, data
stats -> stats_0, stats_1, ...
data -> data_0, data_1, ...
```
