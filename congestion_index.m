speed = [45, 25, 10, 60];
vehicle_count = [20, 50, 100, 15];

congestion_index = vehicle_count .* (1 ./ speed);
disp(congestion_index);
