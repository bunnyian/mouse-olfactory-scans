% Define the folder path where the images will be saved
folderPath = 'C:\Path\to\Parent\Folder';
folderPath = '/Users/ianwu/Documents/MATLAB/OlfactoryScans';

% Iterate over each structure
structures = {'ORdata1_111L', 'ORdata3_112L', 'ORdata5_113L', 'ORdata7_114L'};
for s = 1:numel(structures)
    structureName = structures{s};
    structure = eval(structureName); % Access the structure by its name
    
    % Update PCidnums_maporder
    PCidnums_maporder(186) = 0; % null control
    PCidnums_maporder(187) = 5460048; % triglyceride control

    % Create a subfolder for each odor name
    for i = 1:numel(structure.OdorList)
        cid = PCidnums_maporder(i); % Get the CID
        odorName = num2str(cid); % Convert CID to string
        
        subfolderPath = fullfile(folderPath, odorName); % Modified subfolder path
        if ~exist(subfolderPath, 'dir')
            mkdir(subfolderPath);
        end
        
        % Save the corresponding image for each structure
        map = structure.Maps{i};
        
        % Rotate the image 90 degrees counter-clockwise
        rotatedMap = imrotate(map, -90);
        
        imageName = sprintf('%s.png', structureName); % Modified image name
        imagePath = fullfile(subfolderPath, imageName);
        imwrite(rotatedMap, imagePath);
    end
end