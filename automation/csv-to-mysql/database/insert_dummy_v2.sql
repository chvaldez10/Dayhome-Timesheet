INSERT INTO dayhome_provider (first_name, last_name, location)
VALUES ('chris-parent', 'test', 'chris-parent-test');

INSERT INTO dayhome_children (first_name, last_name, provider_id)
VALUES ('chris-child', 'test', 1);

INSERT INTO dayhome_children_daily_log (
    date_entry,
    sign_in_time,
    sign_out_time,
    total_time,
    status,
    children_id,
    location,
    health_check
)
VALUES (
    '2023-12-15',
    '2023-12-15 08:00:00+00',
    '2023-12-15 17:00:00+00',
    9.0,
    'Present',
    1,
    'chris-parent-test',
    'passed'
);

INSERT INTO dayhome_provider_daily_log (
    date_entry,
    sign_in_time,
    sign_out_time,
    total_time,
    provider_id
)
VALUES (
    '2023-12-15',
    '2023-12-15 08:00:00+00',
    '2023-12-15 17:00:00+00',
    9.0,
    1
);