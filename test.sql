--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

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

--
-- Name: movie_roles; Type: TYPE; Schema: public; Owner: jolo
--

CREATE TYPE public.movie_roles AS ENUM (
    'actor',
    'director'
);


ALTER TYPE public.movie_roles OWNER TO jolo;

--
-- Name: movietagenums; Type: TYPE; Schema: public; Owner: jolo
--

CREATE TYPE public.movietagenums AS ENUM (
    'horror',
    'love',
    'comedy',
    'action'
);


ALTER TYPE public.movietagenums OWNER TO jolo;

--
-- Name: roles; Type: TYPE; Schema: public; Owner: jolo
--

CREATE TYPE public.roles AS ENUM (
    'actor',
    'director'
);


ALTER TYPE public.roles OWNER TO jolo;

--
-- Name: tiers; Type: TYPE; Schema: public; Owner: jolo
--

CREATE TYPE public.tiers AS ENUM (
    'FREE',
    'PRO',
    'ENTERPRISE'
);


ALTER TYPE public.tiers OWNER TO jolo;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: jolo
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO jolo;

--
-- Name: movie_tags; Type: TABLE; Schema: public; Owner: jolo
--

CREATE TABLE public.movie_tags (
    movie_title character varying NOT NULL,
    tag public.movietagenums NOT NULL,
    uuid character varying NOT NULL
);


ALTER TABLE public.movie_tags OWNER TO jolo;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: jolo
--

CREATE TABLE public.movies (
    title character varying NOT NULL,
    ratings double precision NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    uuid character varying NOT NULL,
    CONSTRAINT "rating constraints" CHECK (((ratings > (0)::double precision) AND (ratings <= (5.0)::double precision)))
);


ALTER TABLE public.movies OWNER TO jolo;

--
-- Name: persons; Type: TABLE; Schema: public; Owner: jolo
--

CREATE TABLE public.persons (
    name character varying NOT NULL,
    age integer NOT NULL,
    role public.movie_roles NOT NULL,
    movie_id character varying NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    uuid character varying NOT NULL
);


ALTER TABLE public.persons OWNER TO jolo;

--
-- Name: transactions; Type: TABLE; Schema: public; Owner: jolo
--

CREATE TABLE public.transactions (
    id integer NOT NULL,
    "table" character varying NOT NULL,
    transaction character varying NOT NULL,
    status character varying NOT NULL,
    uuid character varying NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.transactions OWNER TO jolo;

--
-- Name: transactions_id_seq; Type: SEQUENCE; Schema: public; Owner: jolo
--

CREATE SEQUENCE public.transactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.transactions_id_seq OWNER TO jolo;

--
-- Name: transactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jolo
--

ALTER SEQUENCE public.transactions_id_seq OWNED BY public.transactions.id;


--
-- Name: transactions id; Type: DEFAULT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.transactions ALTER COLUMN id SET DEFAULT nextval('public.transactions_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: jolo
--

COPY public.alembic_version (version_num) FROM stdin;
94cc99e2b8cf
\.


--
-- Data for Name: movie_tags; Type: TABLE DATA; Schema: public; Owner: jolo
--

COPY public.movie_tags (movie_title, tag, uuid) FROM stdin;
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: jolo
--

COPY public.movies (title, ratings, created_at, updated_at, uuid) FROM stdin;
Inception	3.4	2025-04-27 19:56:53.683442-04	2025-04-27 19:56:53.683461-04	18237849d4c147aabc5c1f4917e4629f
Titanic	3.4	2025-04-27 19:57:40.366429-04	2025-04-27 19:57:40.366448-04	2ccb94c79277408089681215ff3359c9
Venom	3.4	2025-04-28 01:20:38.548814-04	2025-04-28 01:20:38.548835-04	2ff8813ce7154ddeaba9e7d77606d4a3
Venom 2	3.4	2025-04-28 01:21:01.675122-04	2025-04-28 01:21:01.675145-04	fb17fa3f23c24c208fbebf7ab4ae8ca7
Venom 3	3.4	2025-04-28 01:23:28.178486-04	2025-04-28 01:23:28.178508-04	7dad556c5a3e423b9c75fe98c1e056f9
Naruto	3.4	2025-04-28 02:11:23.154812-04	2025-04-28 02:11:23.154821-04	6e06be2f49604db4ad72d18fd527b4fc
Naruto 2	3.4	2025-04-28 02:14:08.848767-04	2025-04-28 02:14:08.848776-04	684521a9a6e74491a1296ec4e98c7bd8
Naruto 3	3.4	2025-04-28 02:16:47.641441-04	2025-04-28 02:16:47.641455-04	afcb857d92534bbd8dae66d72eb9eb04
Tokyo Ghoul	3.4	2025-04-28 02:17:55.42786-04	2025-04-28 02:17:55.427869-04	fd55fdafb74642368620cead909cbac1
Tokyo Ghoul 2	3.4	2025-04-28 02:20:34.547602-04	2025-04-28 02:20:34.547622-04	a8e7489ce2214fd6bac6f81c6435c22b
Tokyo RE	3.4	2025-04-28 02:22:58.609799-04	2025-04-28 02:22:58.609809-04	5e2b7b45c8914ea2be797b41687e2cc9
Doraemon	3.4	2025-04-28 02:24:37.478719-04	2025-04-28 02:24:37.478726-04	438f5cff5fb543cd982e1080cece3c15
Doraemon Lord	3.4	2025-04-28 02:24:57.105946-04	2025-04-28 02:24:57.105955-04	7e766570f1374a2eac62818c31a5cd72
Doraemon Lord 2	3.4	2025-04-28 02:26:02.676987-04	2025-04-28 02:26:02.676995-04	086ce6f654a74e8492b9477c89b7ef8e
Doraemon Lord 3	3.4	2025-04-28 02:30:21.667296-04	2025-04-28 02:30:21.667305-04	e0eb65fc29944b319861abf1eb59a8c5
\.


--
-- Data for Name: persons; Type: TABLE DATA; Schema: public; Owner: jolo
--

COPY public.persons (name, age, role, movie_id, created_at, updated_at, uuid) FROM stdin;
Leonardo DiCaprio	20	actor	18237849d4c147aabc5c1f4917e4629f	2025-04-27 19:56:53.68886-04	2025-04-27 19:56:53.688867-04	9d53d3e0702045d3a21fe19967ef8967
Joseph Gordon-Levitt	23	director	18237849d4c147aabc5c1f4917e4629f	2025-04-27 19:56:53.688872-04	2025-04-27 19:56:53.688873-04	d919dbf2357548d08f38bbc641e50f93
Leonardo DiCaprio	20	actor	2ccb94c79277408089681215ff3359c9	2025-04-27 19:57:40.369766-04	2025-04-27 19:57:40.369776-04	790c541bab054ef199364267b8a5d676
Joseph Gordon-Levitt	23	director	2ccb94c79277408089681215ff3359c9	2025-04-27 19:57:40.369778-04	2025-04-27 19:57:40.369779-04	5cc718f7e2ff483a82b70b1cc66a05dd
Tom Hardy	28	actor	2ff8813ce7154ddeaba9e7d77606d4a3	2025-04-28 01:20:38.566755-04	2025-04-28 01:20:38.566769-04	aaff1500535444839b623e5a6a7fe4e0
Kristaps Porzingis	33	director	2ff8813ce7154ddeaba9e7d77606d4a3	2025-04-28 01:20:38.566769-04	2025-04-28 01:20:38.56677-04	ecae8302758e4a04ac830d51bdad46ee
Chase Buddinger	13	actor	2ff8813ce7154ddeaba9e7d77606d4a3	2025-04-28 01:20:38.56677-04	2025-04-28 01:20:38.566771-04	5929221969374335977df26b1594eb34
doraemon	10	actor	e0eb65fc29944b319861abf1eb59a8c5	2025-04-28 02:30:21.669046-04	2025-04-28 02:30:21.669051-04	1dd22efa3e3b49bba4fca5f1cea090f7
\.


--
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: jolo
--

COPY public.transactions (id, "table", transaction, status, uuid, created_at, updated_at) FROM stdin;
\.


--
-- Name: transactions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jolo
--

SELECT pg_catalog.setval('public.transactions_id_seq', 1, false);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: movie_tags movie_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.movie_tags
    ADD CONSTRAINT movie_tags_pkey PRIMARY KEY (movie_title, tag, uuid);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (uuid);


--
-- Name: movies movies_title_key; Type: CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_title_key UNIQUE (title);


--
-- Name: persons persons_pkey; Type: CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_pkey PRIMARY KEY (uuid);


--
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (id, uuid);


--
-- Name: movie_tags movie_tags_movie_title_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.movie_tags
    ADD CONSTRAINT movie_tags_movie_title_fkey FOREIGN KEY (movie_title) REFERENCES public.movies(title);


--
-- Name: persons persons_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jolo
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(uuid);


--
-- PostgreSQL database dump complete
--

