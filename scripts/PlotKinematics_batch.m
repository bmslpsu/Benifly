%% Plot Benifly Output
clear;close all;clc
root = 'C:\Users\boc5244\Documents\temp\out';

[FILE,PATH] = uigetfile({'*.csv'},'Select Benifly output .csv', root, 'MultiSelect','on');

FIG = figure (1) ; clf
FIG.Color = 'w';
FIG.Units = 'inches';
FIG.Position = [2 2 7 7];
movegui(FIG,'center')

n = length(FILE);
for kk = 1:n
    filedata = ImportBenifly(fullfile(PATH,FILE{kk}));
    Head(:,kk) = filedata.Head;
    LWing(:,kk) = filedata.LWing;
    RWing(:,kk) = filedata.RWing;
    Abdomen(:,kk) = filedata.Abdomen;
    WBF(:,kk) = filedata.WBF;
end

Head_mean = mean(Head,2);
LWing_mean = mean(LWing,2);
RWing_mean = mean(RWing,2);
Abdomen_mean = mean(Abdomen,2);
WBF_mean = mean(WBF,2);

for kk = 1:n
    filedata = ImportBenifly(fullfile(PATH,FILE{kk}));
    tt = linspace(0,21,size(filedata,1))';
    
    ax(1) = subplot(5,1,1) ; hold on ; title('Head')
    plot(tt, rad2deg(filedata.Head), 'LineWidth', 0.5)

    ax(2) = subplot(5,1,2) ; hold on ; title('Left')
    [filedata.LWing] = hampel(tt,filedata.LWing);
    plot(tt, rad2deg(filedata.LWing), 'LineWidth', 0.5)

    ax(3) = subplot(5,1,3) ; hold on ; title('Right')
    [filedata.RWing] = hampel(tt,filedata.RWing);
    plot(tt, rad2deg(filedata.RWing), 'LineWidth', 0.5)

    ax(4) = subplot(5,1,4) ; hold on ; title('Abdomen')
    plot(tt, rad2deg(filedata.Abdomen), 'LineWidth', 0.5)

    ax(5) = subplot(5,1,5) ; hold on ; title('Aux')
    plot(tt, filedata.WBF, 'LineWidth', 0.5)
    xlabel('Time')
end
axes(ax(1)) ; plot(tt,rad2deg(Head_mean),'k','LineWidth',3')
axes(ax(2)) ; plot(tt,rad2deg(LWing_mean),'k','LineWidth',3')
axes(ax(3)) ; plot(tt,rad2deg(RWing_mean),'k','LineWidth',3')
axes(ax(4)) ; plot(tt,rad2deg(Abdomen_mean),'k','LineWidth',3')
axes(ax(5)) ; plot(tt,WBF_mean,'k','LineWidth',3')

set(ax,'XLim',[0 tt(end)])
set(ax(1),'YLim',20*[-1 1]);
set(ax(2:3),'YLim',[-10 70]);
set(ax(5),'YLim',[0 1]);
linkaxes(ax,'x')
set(ax(1:end-1),'XTickLabels','')
