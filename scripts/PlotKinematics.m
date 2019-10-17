%% Plot Benifly Output
clear;close all;clc
root = 'C:\Users\boc5244\Documents\temp\out';

[file,path] = uigetfile({'*.csv'},'Select Benifly output .csv', root, 'MultiSelect','off');
filedata = ImportBenifly(fullfile(path,file));

FIG = figure (1) ; clf
FIG.Color = 'w';
FIG.Units = 'inches';
FIG.Position = [2 2 7 5];
movegui(FIG,'center')

tt = linspace(0,21,size(filedata,1))';

ax(1) = subplot(5,1,1) ; hold on ; title('Head')
plot(tt, filedata.Head, 'c', 'LineWidth', 1)

ax(2) = subplot(5,1,2) ; hold on ; title('Left')
[filedata.LWing] = hampel(tt,filedata.LWing);
plot(tt, filedata.LWing, 'g', 'LineWidth', 1)

ax(3) = subplot(5,1,3) ; hold on ; title('Right')
[filedata.RWing] = hampel(tt,filedata.RWing);
plot(tt, filedata.RWing, 'r', 'LineWidth', 1)

ax(4) = subplot(5,1,4) ; hold on ; title('Abdomen')
plot(tt, filedata.Abdomen, 'm', 'LineWidth', 1)

ax(5) = subplot(5,1,5) ; hold on ; title('Aux')
plot(tt, filedata.WBF, 'y', 'LineWidth', 1)
xlabel('Time')

set(ax,'XLim',[0 tt(end)])
% set(ax,'YTick',[])
set(ax(1:end-1),'XTickLabels','')