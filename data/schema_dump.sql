--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 13.4 (Ubuntu 13.4-4.pgdg18.04+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id uuid NOT NULL,
    created timestamp with time zone DEFAULT now(),
    modified timestamp with time zone DEFAULT now(),
    name character varying(128) NOT NULL,
    address character varying(128),
    employee_id uuid NOT NULL,
    customer_type_id uuid
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: customer_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer_type (
    id uuid NOT NULL,
    created timestamp with time zone DEFAULT now(),
    modified timestamp with time zone DEFAULT now(),
    name character varying(128) NOT NULL,
    zone character varying(16),
    priority integer
);


ALTER TABLE public.customer_type OWNER TO postgres;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    id uuid NOT NULL,
    created timestamp with time zone DEFAULT now(),
    modified timestamp with time zone DEFAULT now(),
    sesa character varying(128) NOT NULL,
    name character varying(128) NOT NULL
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team (
    id uuid NOT NULL,
    created timestamp with time zone DEFAULT now(),
    modified timestamp with time zone DEFAULT now(),
    name character varying(128) NOT NULL
);


ALTER TABLE public.team OWNER TO postgres;

--
-- Name: team_membership; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_membership (
    id uuid NOT NULL,
    created timestamp with time zone DEFAULT now(),
    modified timestamp with time zone DEFAULT now(),
    employee_id uuid NOT NULL,
    team_id uuid NOT NULL
);


ALTER TABLE public.team_membership OWNER TO postgres;

--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer (id, created, modified, name, address, employee_id, customer_type_id) FROM stdin;
\.


--
-- Data for Name: customer_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_type (id, created, modified, name, zone, priority) FROM stdin;
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (id, created, modified, sesa, name) FROM stdin;
\.


--
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team (id, created, modified, name) FROM stdin;
\.


--
-- Data for Name: team_membership; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.team_membership (id, created, modified, employee_id, team_id) FROM stdin;
\.


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);


--
-- Name: customer_type customer_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer_type
    ADD CONSTRAINT customer_type_pkey PRIMARY KEY (id);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (id);


--
-- Name: employee employee_sesa_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_sesa_key UNIQUE (sesa);


--
-- Name: team_membership team_membership_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_membership
    ADD CONSTRAINT team_membership_pkey PRIMARY KEY (id);


--
-- Name: team team_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_name_key UNIQUE (name);


--
-- Name: team team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (id);


--
-- Name: customer customer_customer_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_customer_type_id_fkey FOREIGN KEY (customer_type_id) REFERENCES public.customer_type(id);


--
-- Name: customer customer_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employee(id);


--
-- Name: team_membership team_membership_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_membership
    ADD CONSTRAINT team_membership_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employee(id);


--
-- Name: team_membership team_membership_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_membership
    ADD CONSTRAINT team_membership_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.team(id);


--
-- PostgreSQL database dump complete
--

