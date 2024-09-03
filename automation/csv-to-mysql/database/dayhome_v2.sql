-- Note: dropping the database and tables will result in data loss
CREATE DATABASE dayhome;

-- Define ENUM type for status 
CREATE TYPE dayhome_status AS ENUM ('present', 'absent', 'sick', 'on_leave'); -- TODO: Change to real values

CREATE TABLE dayhome_provider(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL
);

CREATE TABLE dayhome_children(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    provider_id INTEGER REFERENCES dayhome_provider(id)
);

CREATE TABLE dayhome_children_daily_log(
    id SERIAL PRIMARY KEY,
    date_entry DATE NOT NULL,
    sign_in_time TIMESTAMP WITH TIME ZONE,
    sign_out_time TIMESTAMP WITH TIME ZONE,
    total_time FLOAT CHECK (total_time >= 0) DEFAULT 0,
    status dayhome_status DEFAULT 'absent',
    children_id INTEGER NOT NULL REFERENCES dayhome_children(id),
    health_check VARCHAR(255)
);

CREATE TABLE dayhome_provider_daily_log(
    id SERIAL PRIMARY KEY,
    date_entry DATE NOT NULL,
    sign_in_time TIMESTAMP WITH TIME ZONE,
    sign_out_time TIMESTAMP WITH TIME ZONE,
    total_time FLOAT CHECK (total_time >= 0) DEFAULT 0, -- Ensure non-negative total_time
    provider_id INTEGER NOT NULL REFERENCES dayhome_provider(id)
);

-- Indexes for optimization
CREATE INDEX idx_dailylog_childrenid ON dayhome_children_daily_log (children_id);
CREATE INDEX idx_dailylog_dateentry ON dayhome_children_daily_log (date_entry); -- Index on date_entry for faster date queries

CREATE INDEX idx_providerlog_providerid ON dayhome_provider_daily_log (provider_id);
CREATE INDEX idx_providerlog_dateentry ON dayhome_provider_daily_log (date_entry); -- Index on date_entry for faster date queries
