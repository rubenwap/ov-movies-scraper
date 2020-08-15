SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

CREATE SCHEMA public;
ALTER SCHEMA public OWNER TO postgres;

COMMENT ON SCHEMA public IS 'standard public schema';

SET default_tablespace = '';

SET default_with_oids = false;

CREATE TABLE public.movies (
    cinema character varying(200),
    movie_date character varying(200),
    details character varying(200),
    movie_time character varying(200),
    title character varying(200)
);


ALTER TABLE public.movies OWNER TO postgres;

