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

## Usage
```
from miniseed2mat.miniseed2mat import convertmseed2mat
mseedfile = "myStream.mseed"
convertmseed2mat(mseedfile, output_mat=None)
```

## Read `mat` file in MATLAB

```
clear; close all; clc;

wdir='./';

fileloc0=[wdir,'myStream'];
fileloc_ext = '.mat';
fileloc = [fileloc0 fileloc_ext];

if exist(fileloc,'file')
    disp(['File exists ', fileloc]);
    load(fileloc);
    
    all_stats = fieldnames(stats);
    all_data = fieldnames(data);
    
        
%     for id=1:length(fieldnames(data))
    for id=1
        stats_0 = stats.(all_stats{id});
        data_0 = data.(all_data{id});

        sampling_rate = getfield(stats_0,'sampling_rate');
        delta = getfield(stats_0,'delta');
        starttime = getfield(stats_0,'starttime');
        endtime = getfield(stats_0,'endtime');
        t1 = datetime(starttime,'InputFormat',"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
        t2 = datetime(endtime,'InputFormat',"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
        datetime_array = t1:seconds(delta):t2;

        %% plot time series
        fig = figure('Renderer', 'painters', 'Position', [100 100 1000 400], 'color','w');
        plot(t1:seconds(delta):t2, data_0, 'k-')
        title([getfield(stats_0,'network'),'-', getfield(stats_0,'station'), '-', getfield(stats_0,'channel')])
        axis tight;
        print(fig,['./',fileloc0, '_ts', num2str(id),'.jpg'],'-djpeg')

%         close all;
    end
end

```

![Output Waveforms](myStream_ts1.jpg)
