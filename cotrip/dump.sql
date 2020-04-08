--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-3.pgdg18.04+1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-3.pgdg18.04+1)

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

SET default_with_oids = false;

--
-- Name: Brands_company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Brands_company" (
    id integer NOT NULL,
    company_name character varying(50) NOT NULL,
    username character varying(100) NOT NULL,
    password character varying(20) NOT NULL,
    address character varying(250) NOT NULL,
    zipcode character varying(6) NOT NULL,
    company_logo character varying(100),
    company_landing_imge character varying(100),
    "company_registrationNo" character varying(25) NOT NULL,
    "company_tinnNo" character varying(11),
    "company_vatNo" character varying(13),
    "company_gstNo" character varying(15),
    website character varying(50),
    company_contact_no character varying(15) NOT NULL,
    company_email_id character varying(50) NOT NULL,
    support_person character varying(50),
    support_person_mobileno character varying(15) NOT NULL,
    support_person_email_id character varying(255) NOT NULL,
    support_person_landlineno character varying(15) NOT NULL,
    contact_person character varying(50) NOT NULL,
    contact_person_mobileno character varying(15) NOT NULL,
    contact_person_email_id character varying(255) NOT NULL,
    contact_person_landlineno character varying(15) NOT NULL,
    owner_name character varying(50) NOT NULL,
    owner_email character varying(255) NOT NULL,
    owner_phone character varying(15) NOT NULL,
    billing_address character varying(250),
    is_open boolean NOT NULL,
    active_status boolean NOT NULL,
    is_sound boolean NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    auth_user_id integer,
    billing_city_id integer,
    billing_country_id integer,
    billing_currency_id integer,
    billing_state_id integer,
    business_nature_id integer NOT NULL,
    city_id integer NOT NULL,
    country_id integer NOT NULL,
    state_id integer NOT NULL
);


ALTER TABLE public."Brands_company" OWNER TO postgres;

--
-- Name: Brands_company_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Brands_company_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Brands_company_id_seq" OWNER TO postgres;

--
-- Name: Brands_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Brands_company_id_seq" OWNED BY public."Brands_company".id;


--
-- Name: Configuration_businesstype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Configuration_businesstype" (
    id integer NOT NULL,
    business_type character varying(50) NOT NULL,
    description character varying(200),
    active_status boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone
);


ALTER TABLE public."Configuration_businesstype" OWNER TO postgres;

--
-- Name: Configuration_businesstype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Configuration_businesstype_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Configuration_businesstype_id_seq" OWNER TO postgres;

--
-- Name: Configuration_businesstype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Configuration_businesstype_id_seq" OWNED BY public."Configuration_businesstype".id;


--
-- Name: Configuration_currencymaster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Configuration_currencymaster" (
    id integer NOT NULL,
    currency character varying(30) NOT NULL,
    symbol character varying(20) NOT NULL,
    hexsymbol character varying(7),
    active_status boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone
);


ALTER TABLE public."Configuration_currencymaster" OWNER TO postgres;

--
-- Name: Configuration_currencymaster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Configuration_currencymaster_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Configuration_currencymaster_id_seq" OWNER TO postgres;

--
-- Name: Configuration_currencymaster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Configuration_currencymaster_id_seq" OWNED BY public."Configuration_currencymaster".id;


--
-- Name: Customers_customer_otp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Customers_customer_otp" (
    id integer NOT NULL,
    "mobile_OTP" character varying(10),
    "email_OTP" character varying(10),
    is_mobile_verified boolean NOT NULL,
    is_email_verfied boolean NOT NULL,
    is_email_otp_used boolean NOT NULL,
    is_mob_otp_used boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    customer_id integer
);


ALTER TABLE public."Customers_customer_otp" OWNER TO postgres;

--
-- Name: Customers_customer_otp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Customers_customer_otp_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Customers_customer_otp_id_seq" OWNER TO postgres;

--
-- Name: Customers_customer_otp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Customers_customer_otp_id_seq" OWNED BY public."Customers_customer_otp".id;


--
-- Name: Customers_customerprofile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Customers_customerprofile" (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    password character varying(20) NOT NULL,
    mobile character varying(20),
    name character varying(100),
    email character varying(100),
    age integer,
    profile_pic character varying(100),
    address character varying(150),
    latitude character varying(50),
    longitude character varying(50),
    active_status boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone,
    auth_user_id integer,
    date_of_birth timestamp with time zone,
    gender character varying(100),
    company_id integer NOT NULL,
    CONSTRAINT "Customers_customerprofile_age_check" CHECK ((age >= 0))
);


ALTER TABLE public."Customers_customerprofile" OWNER TO postgres;

--
-- Name: Customers_customerprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Customers_customerprofile_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Customers_customerprofile_id_seq" OWNER TO postgres;

--
-- Name: Customers_customerprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Customers_customerprofile_id_seq" OWNED BY public."Customers_customerprofile".id;


--
-- Name: Location_areamaster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Location_areamaster" (
    id integer NOT NULL,
    area character varying(100) NOT NULL,
    active_status boolean NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    city_id integer NOT NULL
);


ALTER TABLE public."Location_areamaster" OWNER TO postgres;

--
-- Name: Location_areamaster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Location_areamaster_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Location_areamaster_id_seq" OWNER TO postgres;

--
-- Name: Location_areamaster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Location_areamaster_id_seq" OWNED BY public."Location_areamaster".id;


--
-- Name: Location_citymaster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Location_citymaster" (
    id integer NOT NULL,
    city character varying(35) NOT NULL,
    active_status boolean NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    state_id integer NOT NULL
);


ALTER TABLE public."Location_citymaster" OWNER TO postgres;

--
-- Name: Location_citymaster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Location_citymaster_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Location_citymaster_id_seq" OWNER TO postgres;

--
-- Name: Location_citymaster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Location_citymaster_id_seq" OWNED BY public."Location_citymaster".id;


--
-- Name: Location_countrymaster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Location_countrymaster" (
    id integer NOT NULL,
    country character varying(35) NOT NULL,
    iso character varying(4) NOT NULL,
    isd integer NOT NULL,
    mobile_no_digits integer NOT NULL,
    country_flag character varying(100),
    active_status boolean NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    currency_id integer NOT NULL,
    CONSTRAINT "Location_countrymaster_isd_check" CHECK ((isd >= 0)),
    CONSTRAINT "Location_countrymaster_mobile_no_digits_check" CHECK ((mobile_no_digits >= 0))
);


ALTER TABLE public."Location_countrymaster" OWNER TO postgres;

--
-- Name: Location_countrymaster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Location_countrymaster_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Location_countrymaster_id_seq" OWNER TO postgres;

--
-- Name: Location_countrymaster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Location_countrymaster_id_seq" OWNED BY public."Location_countrymaster".id;


--
-- Name: Location_statemaster; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Location_statemaster" (
    id integer NOT NULL,
    state character varying(35) NOT NULL,
    short_name character varying(35) NOT NULL,
    active_status boolean NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    country_id integer
);


ALTER TABLE public."Location_statemaster" OWNER TO postgres;

--
-- Name: Location_statemaster_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Location_statemaster_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Location_statemaster_id_seq" OWNER TO postgres;

--
-- Name: Location_statemaster_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Location_statemaster_id_seq" OWNED BY public."Location_statemaster".id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO postgres;

--
-- Name: dashboard_userdashboardmodule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_userdashboardmodule (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    module character varying(255) NOT NULL,
    app_label character varying(255),
    "user" integer NOT NULL,
    "column" integer NOT NULL,
    "order" integer NOT NULL,
    settings text NOT NULL,
    children text NOT NULL,
    collapsed boolean NOT NULL,
    CONSTRAINT dashboard_userdashboardmodule_column_check CHECK (("column" >= 0)),
    CONSTRAINT dashboard_userdashboardmodule_user_check CHECK (("user" >= 0))
);


ALTER TABLE public.dashboard_userdashboardmodule OWNER TO postgres;

--
-- Name: dashboard_userdashboardmodule_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_userdashboardmodule_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_userdashboardmodule_id_seq OWNER TO postgres;

--
-- Name: dashboard_userdashboardmodule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_userdashboardmodule_id_seq OWNED BY public.dashboard_userdashboardmodule.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: jet_bookmark; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jet_bookmark (
    id integer NOT NULL,
    url character varying(200) NOT NULL,
    title character varying(255) NOT NULL,
    "user" integer NOT NULL,
    date_add timestamp with time zone NOT NULL,
    CONSTRAINT jet_bookmark_user_check CHECK (("user" >= 0))
);


ALTER TABLE public.jet_bookmark OWNER TO postgres;

--
-- Name: jet_bookmark_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jet_bookmark_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.jet_bookmark_id_seq OWNER TO postgres;

--
-- Name: jet_bookmark_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jet_bookmark_id_seq OWNED BY public.jet_bookmark.id;


--
-- Name: jet_pinnedapplication; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jet_pinnedapplication (
    id integer NOT NULL,
    app_label character varying(255) NOT NULL,
    "user" integer NOT NULL,
    date_add timestamp with time zone NOT NULL,
    CONSTRAINT jet_pinnedapplication_user_check CHECK (("user" >= 0))
);


ALTER TABLE public.jet_pinnedapplication OWNER TO postgres;

--
-- Name: jet_pinnedapplication_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jet_pinnedapplication_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.jet_pinnedapplication_id_seq OWNER TO postgres;

--
-- Name: jet_pinnedapplication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jet_pinnedapplication_id_seq OWNED BY public.jet_pinnedapplication.id;


--
-- Name: rest_framework_tracking_apirequestlog; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rest_framework_tracking_apirequestlog (
    id integer NOT NULL,
    requested_at timestamp with time zone NOT NULL,
    response_ms integer NOT NULL,
    path character varying(200) NOT NULL,
    remote_addr inet NOT NULL,
    host character varying(200) NOT NULL,
    method character varying(10) NOT NULL,
    query_params text,
    data text,
    response text,
    status_code integer,
    user_id integer,
    view character varying(200),
    view_method character varying(27),
    errors text,
    CONSTRAINT rest_framework_tracking_apirequestlog_response_ms_check CHECK ((response_ms >= 0)),
    CONSTRAINT rest_framework_tracking_apirequestlog_status_code_check CHECK ((status_code >= 0))
);


ALTER TABLE public.rest_framework_tracking_apirequestlog OWNER TO postgres;

--
-- Name: rest_framework_tracking_apirequestlog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rest_framework_tracking_apirequestlog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rest_framework_tracking_apirequestlog_id_seq OWNER TO postgres;

--
-- Name: rest_framework_tracking_apirequestlog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rest_framework_tracking_apirequestlog_id_seq OWNED BY public.rest_framework_tracking_apirequestlog.id;


--
-- Name: Brands_company id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company" ALTER COLUMN id SET DEFAULT nextval('public."Brands_company_id_seq"'::regclass);


--
-- Name: Configuration_businesstype id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Configuration_businesstype" ALTER COLUMN id SET DEFAULT nextval('public."Configuration_businesstype_id_seq"'::regclass);


--
-- Name: Configuration_currencymaster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Configuration_currencymaster" ALTER COLUMN id SET DEFAULT nextval('public."Configuration_currencymaster_id_seq"'::regclass);


--
-- Name: Customers_customer_otp id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customer_otp" ALTER COLUMN id SET DEFAULT nextval('public."Customers_customer_otp_id_seq"'::regclass);


--
-- Name: Customers_customerprofile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customerprofile" ALTER COLUMN id SET DEFAULT nextval('public."Customers_customerprofile_id_seq"'::regclass);


--
-- Name: Location_areamaster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_areamaster" ALTER COLUMN id SET DEFAULT nextval('public."Location_areamaster_id_seq"'::regclass);


--
-- Name: Location_citymaster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_citymaster" ALTER COLUMN id SET DEFAULT nextval('public."Location_citymaster_id_seq"'::regclass);


--
-- Name: Location_countrymaster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_countrymaster" ALTER COLUMN id SET DEFAULT nextval('public."Location_countrymaster_id_seq"'::regclass);


--
-- Name: Location_statemaster id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_statemaster" ALTER COLUMN id SET DEFAULT nextval('public."Location_statemaster_id_seq"'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: dashboard_userdashboardmodule id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_userdashboardmodule ALTER COLUMN id SET DEFAULT nextval('public.dashboard_userdashboardmodule_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: jet_bookmark id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jet_bookmark ALTER COLUMN id SET DEFAULT nextval('public.jet_bookmark_id_seq'::regclass);


--
-- Name: jet_pinnedapplication id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jet_pinnedapplication ALTER COLUMN id SET DEFAULT nextval('public.jet_pinnedapplication_id_seq'::regclass);


--
-- Name: rest_framework_tracking_apirequestlog id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rest_framework_tracking_apirequestlog ALTER COLUMN id SET DEFAULT nextval('public.rest_framework_tracking_apirequestlog_id_seq'::regclass);


--
-- Data for Name: Brands_company; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Brands_company" (id, company_name, username, password, address, zipcode, company_logo, company_landing_imge, "company_registrationNo", "company_tinnNo", "company_vatNo", "company_gstNo", website, company_contact_no, company_email_id, support_person, support_person_mobileno, support_person_email_id, support_person_landlineno, contact_person, contact_person_mobileno, contact_person_email_id, contact_person_landlineno, owner_name, owner_email, owner_phone, billing_address, is_open, active_status, is_sound, created_at, updated_at, auth_user_id, billing_city_id, billing_country_id, billing_currency_id, billing_state_id, business_nature_id, city_id, country_id, state_id) FROM stdin;
1	Mapple	mapple	123456	B 65/1 hari nagar ashram	110014			234324324324	\N	\N	\N	\N	08750477098	umeshsamal3@gmail.com	\N	08750477098	umeshsamal3@gmail.com	32424324	umesh samal	08750477098	umeshsamal3@gmail.com	34243232	mapple	abc@gmail.com	3242423	\N	t	t	f	2020-03-24 17:02:09.952695+05:30	\N	3	1	1	1	1	1	1	1	1
\.


--
-- Data for Name: Configuration_businesstype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Configuration_businesstype" (id, business_type, description, active_status, created_at, updated_at) FROM stdin;
1	Social Service	\N	t	2020-03-24 16:52:01.449291+05:30	\N
\.


--
-- Data for Name: Configuration_currencymaster; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Configuration_currencymaster" (id, currency, symbol, hexsymbol, active_status, created_at, updated_at) FROM stdin;
1	yen	平仮名	\N	t	2020-03-24 16:56:24.88596+05:30	\N
\.


--
-- Data for Name: Customers_customer_otp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Customers_customer_otp" (id, "mobile_OTP", "email_OTP", is_mobile_verified, is_email_verfied, is_email_otp_used, is_mob_otp_used, created_at, customer_id) FROM stdin;
\.


--
-- Data for Name: Customers_customerprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Customers_customerprofile" (id, username, password, mobile, name, email, age, profile_pic, address, latitude, longitude, active_status, created_at, updated_at, auth_user_id, date_of_birth, gender, company_id) FROM stdin;
1	1Mumesh	123456	8750477098	umesh	umeshsamal13@gmail.com	19		delhi	\N	\N	t	2020-03-24 17:03:16.866924+05:30	2020-03-24 17:17:52.434652+05:30	\N	2000-09-22 05:30:00+05:30	male	1
\.


--
-- Data for Name: Location_areamaster; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Location_areamaster" (id, area, active_status, created_at, updated_at, city_id) FROM stdin;
\.


--
-- Data for Name: Location_citymaster; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Location_citymaster" (id, city, active_status, created_at, updated_at, state_id) FROM stdin;
1	Tokyo	t	2020-03-24 16:58:31.335584+05:30	\N	1
\.


--
-- Data for Name: Location_countrymaster; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Location_countrymaster" (id, country, iso, isd, mobile_no_digits, country_flag, active_status, created_at, updated_at, currency_id) FROM stdin;
1	Japan	JPN	81	11		t	2020-03-24 16:57:05.315543+05:30	\N	1
\.


--
-- Data for Name: Location_statemaster; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Location_statemaster" (id, state, short_name, active_status, created_at, updated_at, country_id) FROM stdin;
1	Shizuoka	Shizuoka	t	2020-03-24 16:57:59.215479+05:30	\N	1
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add user dashboard module	1	add_userdashboardmodule
2	Can change user dashboard module	1	change_userdashboardmodule
3	Can delete user dashboard module	1	delete_userdashboardmodule
4	Can view user dashboard module	1	view_userdashboardmodule
5	Can add bookmark	2	add_bookmark
6	Can change bookmark	2	change_bookmark
7	Can delete bookmark	2	delete_bookmark
8	Can view bookmark	2	view_bookmark
9	Can add pinned application	3	add_pinnedapplication
10	Can change pinned application	3	change_pinnedapplication
11	Can delete pinned application	3	delete_pinnedapplication
12	Can view pinned application	3	view_pinnedapplication
13	Can add log entry	4	add_logentry
14	Can change log entry	4	change_logentry
15	Can delete log entry	4	delete_logentry
16	Can view log entry	4	view_logentry
17	Can add permission	5	add_permission
18	Can change permission	5	change_permission
19	Can delete permission	5	delete_permission
20	Can view permission	5	view_permission
21	Can add group	6	add_group
22	Can change group	6	change_group
23	Can delete group	6	delete_group
24	Can view group	6	view_group
25	Can add user	7	add_user
26	Can change user	7	change_user
27	Can delete user	7	delete_user
28	Can view user	7	view_user
29	Can add content type	8	add_contenttype
30	Can change content type	8	change_contenttype
31	Can delete content type	8	delete_contenttype
32	Can view content type	8	view_contenttype
33	Can add session	9	add_session
34	Can change session	9	change_session
35	Can delete session	9	delete_session
36	Can view session	9	view_session
37	Can add Token	10	add_token
38	Can change Token	10	change_token
39	Can delete Token	10	delete_token
40	Can view Token	10	view_token
41	Can add API Request Log	11	add_apirequestlog
42	Can change API Request Log	11	change_apirequestlog
43	Can delete API Request Log	11	delete_apirequestlog
44	Can view API Request Log	11	view_apirequestlog
45	Can add Brand	12	add_company
46	Can change Brand	12	change_company
47	Can delete Brand	12	delete_company
48	Can view Brand	12	view_company
49	Can add     Brand Type	13	add_businesstype
50	Can change     Brand Type	13	change_businesstype
51	Can delete     Brand Type	13	delete_businesstype
52	Can view     Brand Type	13	view_businesstype
53	Can add    Currency	14	add_currencymaster
54	Can change    Currency	14	change_currencymaster
55	Can delete    Currency	14	delete_currencymaster
56	Can view    Currency	14	view_currencymaster
57	Can add  Customer OTP	15	add_customer_otp
58	Can change  Customer OTP	15	change_customer_otp
59	Can delete  Customer OTP	15	delete_customer_otp
60	Can view  Customer OTP	15	view_customer_otp
61	Can add Customer	16	add_customerprofile
62	Can change Customer	16	change_customerprofile
63	Can delete Customer	16	delete_customerprofile
64	Can view Customer	16	view_customerprofile
65	Can add Locality	17	add_areamaster
66	Can change Locality	17	change_areamaster
67	Can delete Locality	17	delete_areamaster
68	Can view Locality	17	view_areamaster
69	Can add  City	18	add_citymaster
70	Can change  City	18	change_citymaster
71	Can delete  City	18	delete_citymaster
72	Can view  City	18	view_citymaster
73	Can add    Country	19	add_countrymaster
74	Can change    Country	19	change_countrymaster
75	Can delete    Country	19	delete_countrymaster
76	Can view    Country	19	view_countrymaster
77	Can add   State	20	add_statemaster
78	Can change   State	20	change_statemaster
79	Can delete   State	20	delete_statemaster
80	Can view   State	20	view_statemaster
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$120000$ofvSROU9tRvw$2X2gOOn388sVx7LpNckTmJTVKHcMBmJZRMYg/OpKtJ8=	2020-03-24 16:54:34.244322+05:30	t	umesh			umeshsamal3@gmail.com	t	t	2020-03-24 16:45:26.249713+05:30
3	pbkdf2_sha256$120000$lS8nMj4Aqp4v$lGEJhSDH4faMpxDhgRVMh7ATsB9QEqcZjdrdvLV2WQ0=	\N	f	mapple				f	t	2020-03-24 17:02:09.860222+05:30
4	pbkdf2_sha256$120000$mhfJaPBt39JN$pneVZwRizkokdfSGI7auoDfGhFYsR3xfio65RVn7RHs=	2020-03-24 17:22:30.849088+05:30	f	1Mumesh			umeshsamal13@gmail.com	f	t	2020-03-24 17:03:16.757321+05:30
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
a993d2ae401f6888200caa634603b135d1406180	2020-03-24 17:17:56.07722+05:30	4
\.


--
-- Data for Name: dashboard_userdashboardmodule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_userdashboardmodule (id, title, module, app_label, "user", "column", "order", settings, children, collapsed) FROM stdin;
1	Quick links	jet.dashboard.modules.LinkList	\N	1	0	0	{"draggable": false, "deletable": false, "collapsible": false, "layout": "inline"}	[{"title": "Return to site", "url": "/"}, {"title": "Change password", "url": "/password_change/"}, {"title": "Log out", "url": "/logout/"}]	f
2	Applications	jet.dashboard.modules.AppList	\N	1	1	0	{"models": null, "exclude": ["auth.*"]}		f
3	Administration	jet.dashboard.modules.AppList	\N	1	2	0	{"models": ["auth.*"], "exclude": null}		f
4	Recent Actions	jet.dashboard.modules.RecentActions	\N	1	0	1	{"limit": 10, "include_list": null, "exclude_list": null, "user": null}		f
5	Latest Django News	jet.dashboard.modules.Feed	\N	1	1	1	{"feed_url": "http://www.djangoproject.com/rss/weblog/", "limit": 5}		f
6	Support	jet.dashboard.modules.LinkList	\N	1	2	1	{"draggable": true, "deletable": true, "collapsible": true, "layout": "stacked"}	[{"title": "Django documentation", "url": "http://docs.djangoproject.com/", "external": true}, {"title": "Django \\"django-users\\" mailing list", "url": "http://groups.google.com/group/django-users", "external": true}, {"title": "Django irc channel", "url": "irc://irc.freenode.net/django", "external": true}]	f
7	Application models	jet.dashboard.modules.ModelList	Configuration	1	0	0	{"models": ["Configuration.*"], "exclude": null}		f
8	Recent Actions	jet.dashboard.modules.RecentActions	Configuration	1	1	0	{"limit": 10, "include_list": ["Configuration.*"], "exclude_list": null, "user": null}		f
9	Application models	jet.dashboard.modules.ModelList	Brands	1	0	0	{"models": ["Brands.*"], "exclude": null}		f
10	Recent Actions	jet.dashboard.modules.RecentActions	Brands	1	1	0	{"limit": 10, "include_list": ["Brands.*"], "exclude_list": null, "user": null}		f
11	Application models	jet.dashboard.modules.ModelList	Customers	1	0	0	{"models": ["Customers.*"], "exclude": null}		f
12	Recent Actions	jet.dashboard.modules.RecentActions	Customers	1	1	0	{"limit": 10, "include_list": ["Customers.*"], "exclude_list": null, "user": null}		f
13	Application models	jet.dashboard.modules.ModelList	Location	1	0	0	{"models": ["Location.*"], "exclude": null}		f
14	Recent Actions	jet.dashboard.modules.RecentActions	Location	1	1	0	{"limit": 10, "include_list": ["Location.*"], "exclude_list": null, "user": null}		f
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-03-24 16:52:01.45065+05:30	1	Social Service	1	[{"added": {}}]	13	1
2	2020-03-24 16:56:24.889563+05:30	1	yen	1	[{"added": {}}]	14	1
3	2020-03-24 16:57:05.31695+05:30	1	Japan	1	[{"added": {}}]	19	1
4	2020-03-24 16:57:59.216452+05:30	1	Shizuoka	1	[{"added": {}}]	20	1
5	2020-03-24 16:58:31.338989+05:30	1	Tokyo	1	[{"added": {}}]	18	1
6	2020-03-24 17:02:09.953984+05:30	1	Mapple	1	[{"added": {}}]	12	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	dashboard	userdashboardmodule
2	jet	bookmark
3	jet	pinnedapplication
4	admin	logentry
5	auth	permission
6	auth	group
7	auth	user
8	contenttypes	contenttype
9	sessions	session
10	authtoken	token
11	rest_framework_tracking	apirequestlog
12	Brands	company
13	Configuration	businesstype
14	Configuration	currencymaster
15	Customers	customer_otp
16	Customers	customerprofile
17	Location	areamaster
18	Location	citymaster
19	Location	countrymaster
20	Location	statemaster
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-03-24 16:44:30.863994+05:30
2	auth	0001_initial	2020-03-24 16:44:31.877592+05:30
3	Configuration	0001_initial	2020-03-24 16:44:32.208472+05:30
4	Location	0001_initial	2020-03-24 16:44:32.778802+05:30
5	Brands	0001_initial	2020-03-24 16:44:33.44642+05:30
6	Customers	0001_initial	2020-03-24 16:44:33.980466+05:30
7	Customers	0002_customerprofile_date_of_birth	2020-03-24 16:44:34.033077+05:30
8	Customers	0003_auto_20200324_1058	2020-03-24 16:44:34.08837+05:30
9	Customers	0004_customerprofile_gender	2020-03-24 16:44:34.110454+05:30
10	Customers	0005_customerprofile_company	2020-03-24 16:44:34.224617+05:30
11	admin	0001_initial	2020-03-24 16:44:34.475382+05:30
12	admin	0002_logentry_remove_auto_add	2020-03-24 16:44:34.554442+05:30
13	admin	0003_logentry_add_action_flag_choices	2020-03-24 16:44:34.577097+05:30
14	contenttypes	0002_remove_content_type_name	2020-03-24 16:44:34.622156+05:30
15	auth	0002_alter_permission_name_max_length	2020-03-24 16:44:34.644516+05:30
16	auth	0003_alter_user_email_max_length	2020-03-24 16:44:34.69984+05:30
17	auth	0004_alter_user_username_opts	2020-03-24 16:44:34.720915+05:30
18	auth	0005_alter_user_last_login_null	2020-03-24 16:44:34.755538+05:30
19	auth	0006_require_contenttypes_0002	2020-03-24 16:44:34.766715+05:30
20	auth	0007_alter_validators_add_error_messages	2020-03-24 16:44:34.789102+05:30
21	auth	0008_alter_user_username_max_length	2020-03-24 16:44:34.856232+05:30
22	auth	0009_alter_user_last_name_max_length	2020-03-24 16:44:34.911603+05:30
23	authtoken	0001_initial	2020-03-24 16:44:35.069632+05:30
24	authtoken	0002_auto_20160226_1747	2020-03-24 16:44:35.16698+05:30
25	dashboard	0001_initial	2020-03-24 16:44:35.270014+05:30
26	jet	0001_initial	2020-03-24 16:44:35.483627+05:30
27	jet	0002_delete_userdashboardmodule	2020-03-24 16:44:35.518664+05:30
28	rest_framework_tracking	0001_initial	2020-03-24 16:44:35.817951+05:30
29	rest_framework_tracking	0002_auto_20170118_1713	2020-03-24 16:44:36.073015+05:30
30	rest_framework_tracking	0003_add_errors	2020-03-24 16:44:36.137011+05:30
31	rest_framework_tracking	0004_add_verbose_name	2020-03-24 16:44:36.159256+05:30
32	rest_framework_tracking	0005_auto_20171219_1537	2020-03-24 16:44:36.203595+05:30
33	rest_framework_tracking	0006_view_and_view_method_nullable	2020-03-24 16:44:36.731951+05:30
34	rest_framework_tracking	0006_auto_20180315_1442	2020-03-24 16:44:36.815273+05:30
35	rest_framework_tracking	0007_merge_20180419_1646	2020-03-24 16:44:36.826338+05:30
36	sessions	0001_initial	2020-03-24 16:44:37.029317+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
cgdpmq5r38icgzlpq5hmri5mgwxocfg5	MTFjZWE1MWIwNDI5MDgwNDBkOWNmZjE4MGI3ZDIwZDE2NDZmNDYzNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDBiMmQ1YzRkZWY2YzFhN2M2ZGQ2YzdlMjZkOGNhNjhlZjRhMzgwIn0=	2020-04-07 16:54:34.396304+05:30
4sud3tbrxv8mgc5sdynszpqpocbnhjx9	NDc0Y2E0NmU1YjNlYTczYTg3MDI0MmExODhhMTU0M2M3ODBlZTZiZTp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1NGZhMTM2Njg5OTY5ZDU1Y2YyNGZjMTQwYzg3ZmQyNmM3ZTk5Yjc5In0=	2020-04-07 17:22:30.877494+05:30
\.


--
-- Data for Name: jet_bookmark; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jet_bookmark (id, url, title, "user", date_add) FROM stdin;
\.


--
-- Data for Name: jet_pinnedapplication; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jet_pinnedapplication (id, app_label, "user", date_add) FROM stdin;
\.


--
-- Data for Name: rest_framework_tracking_apirequestlog; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rest_framework_tracking_apirequestlog (id, requested_at, response_ms, path, remote_addr, host, method, query_params, data, response, status_code, user_id, view, view_method, errors) FROM stdin;
1	2020-03-24 16:47:30.65076+05:30	0	/api/mapple/signup/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'mobile': '8750477098', 'password': '********************', 'email': 'umeshsamal3@gmail.com', 'date_of_birth': '2019-09-22', 'address': 'delhi', 'gender': 'male'}	{"success":false,"message":"Error happened!!","errors":"name 'data' is not defined"}	200	\N	MappleApi.Api.Authorization.register.Signup	post	\N
2	2020-03-24 16:47:55.403639+05:30	4	/api/mapple/signup/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'mobile': '8750477098', 'password': '********************', 'email': 'umeshsamal3@gmail.com', 'date_of_birth': '2019-09-22', 'address': 'delhi', 'gender': 'male'}	{"error":{"username":null,"email":null,"password":null,"mobile":null,"age":"Age is not Valid!!"},"message":"Please correct listed errors!!"}	200	\N	MappleApi.Api.Authorization.register.Signup	post	\N
3	2020-03-24 16:48:05.647867+05:30	12	/api/mapple/signup/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'mobile': '8750477098', 'password': '********************', 'email': 'umeshsamal3@gmail.com', 'date_of_birth': '2000-09-22', 'address': 'delhi', 'gender': 'male'}	{"success":false,"message":"User with the entered email already exists!!"}	200	\N	MappleApi.Api.Authorization.register.Signup	post	\N
4	2020-03-24 16:50:20.827964+05:30	14	/api/mapple/signup/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'mobile': '8750477098', 'password': '********************', 'email': 'umeshsamal3@gmail.com', 'date_of_birth': '2000-09-22', 'address': 'delhi', 'gender': 'male'}	{"success":false,"message":"User with the entered email already exists!!"}	200	\N	MappleApi.Api.Authorization.register.Signup	post	\N
5	2020-03-24 16:50:25.03666+05:30	141	/api/mapple/signup/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'mobile': '8750477098', 'password': '********************', 'email': 'umeshsamal13@gmail.com', 'date_of_birth': '2000-09-22', 'address': 'delhi', 'gender': 'male'}	{"success":false,"message":"{'company': [ErrorDetail(string='Invalid pk \\"1\\" - object does not exist.', code='does_not_exist')]}"}	200	\N	MappleApi.Api.Authorization.register.Signup	post	\N
6	2020-03-24 17:02:18.613581+05:30	8	/api/mapple/signup/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'mobile': '8750477098', 'password': '********************', 'email': 'umeshsamal13@gmail.com', 'date_of_birth': '2000-09-22', 'address': 'delhi', 'gender': 'male'}	{"success":false,"message":"User already exists..Please login directly!!"}	200	\N	MappleApi.Api.Authorization.register.Signup	post	\N
7	2020-03-24 17:03:16.747649+05:30	124	/api/mapple/signup/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'mobile': '8750477098', 'password': '********************', 'email': 'umeshsamal13@gmail.com', 'date_of_birth': '2000-09-22', 'address': 'delhi', 'gender': 'male'}	{"success":true,"message":"You have been registered successfully.!!"}	200	\N	MappleApi.Api.Authorization.register.Signup	post	\N
8	2020-03-24 17:22:18.563801+05:30	0	/api/customer/signin/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': '', 'password': '********************'}	{"success":false,"error":{"username":"Please enter your Username!!","password":"Please enter your Password!!"},"message":"Please correct listed errors!!"}	200	\N	MappleApi.Api.Authorization.auth.SignIn	post	\N
9	2020-03-24 17:22:30.713249+05:30	154	/api/customer/signin/	192.168.0.17	192.168.0.17:1111	POST	{}	{'username': 'umesh', 'password': '********************'}	{"success":true,"credential":true,"message":"You are logged in now!!","token":"a993d2ae401f6888200caa634603b135d1406180","user_id":4}	200	4	MappleApi.Api.Authorization.auth.SignIn	post	\N
\.


--
-- Name: Brands_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Brands_company_id_seq"', 1, true);


--
-- Name: Configuration_businesstype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Configuration_businesstype_id_seq"', 1, true);


--
-- Name: Configuration_currencymaster_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Configuration_currencymaster_id_seq"', 1, true);


--
-- Name: Customers_customer_otp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Customers_customer_otp_id_seq"', 1, false);


--
-- Name: Customers_customerprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Customers_customerprofile_id_seq"', 1, true);


--
-- Name: Location_areamaster_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Location_areamaster_id_seq"', 1, false);


--
-- Name: Location_citymaster_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Location_citymaster_id_seq"', 1, true);


--
-- Name: Location_countrymaster_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Location_countrymaster_id_seq"', 1, true);


--
-- Name: Location_statemaster_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Location_statemaster_id_seq"', 1, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 80, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 4, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: dashboard_userdashboardmodule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_userdashboardmodule_id_seq', 14, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 6, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 20, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 36, true);


--
-- Name: jet_bookmark_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jet_bookmark_id_seq', 1, false);


--
-- Name: jet_pinnedapplication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jet_pinnedapplication_id_seq', 1, false);


--
-- Name: rest_framework_tracking_apirequestlog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rest_framework_tracking_apirequestlog_id_seq', 9, true);


--
-- Name: Brands_company Brands_company_auth_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_auth_user_id_key" UNIQUE (auth_user_id);


--
-- Name: Brands_company Brands_company_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_pkey" PRIMARY KEY (id);


--
-- Name: Brands_company Brands_company_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_username_key" UNIQUE (username);


--
-- Name: Configuration_businesstype Configuration_businesstype_business_type_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Configuration_businesstype"
    ADD CONSTRAINT "Configuration_businesstype_business_type_key" UNIQUE (business_type);


--
-- Name: Configuration_businesstype Configuration_businesstype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Configuration_businesstype"
    ADD CONSTRAINT "Configuration_businesstype_pkey" PRIMARY KEY (id);


--
-- Name: Configuration_currencymaster Configuration_currencymaster_currency_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Configuration_currencymaster"
    ADD CONSTRAINT "Configuration_currencymaster_currency_key" UNIQUE (currency);


--
-- Name: Configuration_currencymaster Configuration_currencymaster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Configuration_currencymaster"
    ADD CONSTRAINT "Configuration_currencymaster_pkey" PRIMARY KEY (id);


--
-- Name: Customers_customer_otp Customers_customer_otp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customer_otp"
    ADD CONSTRAINT "Customers_customer_otp_pkey" PRIMARY KEY (id);


--
-- Name: Customers_customerprofile Customers_customerprofile_age_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customerprofile"
    ADD CONSTRAINT "Customers_customerprofile_age_key" UNIQUE (age);


--
-- Name: Customers_customerprofile Customers_customerprofile_auth_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customerprofile"
    ADD CONSTRAINT "Customers_customerprofile_auth_user_id_key" UNIQUE (auth_user_id);


--
-- Name: Customers_customerprofile Customers_customerprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customerprofile"
    ADD CONSTRAINT "Customers_customerprofile_pkey" PRIMARY KEY (id);


--
-- Name: Customers_customerprofile Customers_customerprofile_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customerprofile"
    ADD CONSTRAINT "Customers_customerprofile_username_key" UNIQUE (username);


--
-- Name: Location_areamaster Location_areamaster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_areamaster"
    ADD CONSTRAINT "Location_areamaster_pkey" PRIMARY KEY (id);


--
-- Name: Location_citymaster Location_citymaster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_citymaster"
    ADD CONSTRAINT "Location_citymaster_pkey" PRIMARY KEY (id);


--
-- Name: Location_citymaster Location_citymaster_state_id_city_e2b8a27b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_citymaster"
    ADD CONSTRAINT "Location_citymaster_state_id_city_e2b8a27b_uniq" UNIQUE (state_id, city);


--
-- Name: Location_countrymaster Location_countrymaster_country_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_countrymaster"
    ADD CONSTRAINT "Location_countrymaster_country_key" UNIQUE (country);


--
-- Name: Location_countrymaster Location_countrymaster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_countrymaster"
    ADD CONSTRAINT "Location_countrymaster_pkey" PRIMARY KEY (id);


--
-- Name: Location_statemaster Location_statemaster_country_id_state_5f92d147_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_statemaster"
    ADD CONSTRAINT "Location_statemaster_country_id_state_5f92d147_uniq" UNIQUE (country_id, state);


--
-- Name: Location_statemaster Location_statemaster_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_statemaster"
    ADD CONSTRAINT "Location_statemaster_pkey" PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: dashboard_userdashboardmodule dashboard_userdashboardmodule_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_userdashboardmodule
    ADD CONSTRAINT dashboard_userdashboardmodule_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: jet_bookmark jet_bookmark_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jet_bookmark
    ADD CONSTRAINT jet_bookmark_pkey PRIMARY KEY (id);


--
-- Name: jet_pinnedapplication jet_pinnedapplication_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jet_pinnedapplication
    ADD CONSTRAINT jet_pinnedapplication_pkey PRIMARY KEY (id);


--
-- Name: rest_framework_tracking_apirequestlog rest_framework_tracking_apirequestlog_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rest_framework_tracking_apirequestlog
    ADD CONSTRAINT rest_framework_tracking_apirequestlog_pkey PRIMARY KEY (id);


--
-- Name: Brands_company_billing_city_id_887b799f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_billing_city_id_887b799f" ON public."Brands_company" USING btree (billing_city_id);


--
-- Name: Brands_company_billing_country_id_e6ce75bd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_billing_country_id_e6ce75bd" ON public."Brands_company" USING btree (billing_country_id);


--
-- Name: Brands_company_billing_currency_id_dcaac728; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_billing_currency_id_dcaac728" ON public."Brands_company" USING btree (billing_currency_id);


--
-- Name: Brands_company_billing_state_id_13c0ff27; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_billing_state_id_13c0ff27" ON public."Brands_company" USING btree (billing_state_id);


--
-- Name: Brands_company_business_nature_id_74523f18; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_business_nature_id_74523f18" ON public."Brands_company" USING btree (business_nature_id);


--
-- Name: Brands_company_city_id_04cd5a1a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_city_id_04cd5a1a" ON public."Brands_company" USING btree (city_id);


--
-- Name: Brands_company_country_id_50088a31; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_country_id_50088a31" ON public."Brands_company" USING btree (country_id);


--
-- Name: Brands_company_state_id_dd39f16b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_state_id_dd39f16b" ON public."Brands_company" USING btree (state_id);


--
-- Name: Brands_company_username_150b66b5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Brands_company_username_150b66b5_like" ON public."Brands_company" USING btree (username varchar_pattern_ops);


--
-- Name: Configuration_businesstype_business_type_5bf02705_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Configuration_businesstype_business_type_5bf02705_like" ON public."Configuration_businesstype" USING btree (business_type varchar_pattern_ops);


--
-- Name: Configuration_currencymaster_currency_421719bb_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Configuration_currencymaster_currency_421719bb_like" ON public."Configuration_currencymaster" USING btree (currency varchar_pattern_ops);


--
-- Name: Customers_customer_otp_customer_id_4a5ab955; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Customers_customer_otp_customer_id_4a5ab955" ON public."Customers_customer_otp" USING btree (customer_id);


--
-- Name: Customers_customerprofile_company_id_e735d378; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Customers_customerprofile_company_id_e735d378" ON public."Customers_customerprofile" USING btree (company_id);


--
-- Name: Customers_customerprofile_username_251e0704_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Customers_customerprofile_username_251e0704_like" ON public."Customers_customerprofile" USING btree (username varchar_pattern_ops);


--
-- Name: Location_areamaster_city_id_6a460ea6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Location_areamaster_city_id_6a460ea6" ON public."Location_areamaster" USING btree (city_id);


--
-- Name: Location_citymaster_state_id_6ab4cb92; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Location_citymaster_state_id_6ab4cb92" ON public."Location_citymaster" USING btree (state_id);


--
-- Name: Location_countrymaster_country_992d8acd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Location_countrymaster_country_992d8acd_like" ON public."Location_countrymaster" USING btree (country varchar_pattern_ops);


--
-- Name: Location_countrymaster_currency_id_91e69f4c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Location_countrymaster_currency_id_91e69f4c" ON public."Location_countrymaster" USING btree (currency_id);


--
-- Name: Location_statemaster_country_id_0ba51b0a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "Location_statemaster_country_id_0ba51b0a" ON public."Location_statemaster" USING btree (country_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: rest_framework_tracking_apirequestlog_path_fe81f91b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_path_fe81f91b ON public.rest_framework_tracking_apirequestlog USING btree (path);


--
-- Name: rest_framework_tracking_apirequestlog_path_fe81f91b_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_path_fe81f91b_like ON public.rest_framework_tracking_apirequestlog USING btree (path varchar_pattern_ops);


--
-- Name: rest_framework_tracking_apirequestlog_requested_at_b6f1c2f2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_requested_at_b6f1c2f2 ON public.rest_framework_tracking_apirequestlog USING btree (requested_at);


--
-- Name: rest_framework_tracking_apirequestlog_user_id_671b70b7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_user_id_671b70b7 ON public.rest_framework_tracking_apirequestlog USING btree (user_id);


--
-- Name: rest_framework_tracking_apirequestlog_view_5bd1e407; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_view_5bd1e407 ON public.rest_framework_tracking_apirequestlog USING btree (view);


--
-- Name: rest_framework_tracking_apirequestlog_view_5bd1e407_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_view_5bd1e407_like ON public.rest_framework_tracking_apirequestlog USING btree (view varchar_pattern_ops);


--
-- Name: rest_framework_tracking_apirequestlog_view_method_dd790881; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_view_method_dd790881 ON public.rest_framework_tracking_apirequestlog USING btree (view_method);


--
-- Name: rest_framework_tracking_apirequestlog_view_method_dd790881_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX rest_framework_tracking_apirequestlog_view_method_dd790881_like ON public.rest_framework_tracking_apirequestlog USING btree (view_method varchar_pattern_ops);


--
-- Name: Brands_company Brands_company_auth_user_id_ff2c4be3_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_auth_user_id_ff2c4be3_fk_auth_user_id" FOREIGN KEY (auth_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_billing_city_id_887b799f_fk_Location_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_billing_city_id_887b799f_fk_Location_" FOREIGN KEY (billing_city_id) REFERENCES public."Location_citymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_billing_country_id_e6ce75bd_fk_Location_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_billing_country_id_e6ce75bd_fk_Location_" FOREIGN KEY (billing_country_id) REFERENCES public."Location_countrymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_billing_currency_id_dcaac728_fk_Configura; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_billing_currency_id_dcaac728_fk_Configura" FOREIGN KEY (billing_currency_id) REFERENCES public."Configuration_currencymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_billing_state_id_13c0ff27_fk_Location_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_billing_state_id_13c0ff27_fk_Location_" FOREIGN KEY (billing_state_id) REFERENCES public."Location_statemaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_business_nature_id_74523f18_fk_Configura; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_business_nature_id_74523f18_fk_Configura" FOREIGN KEY (business_nature_id) REFERENCES public."Configuration_businesstype"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_city_id_04cd5a1a_fk_Location_citymaster_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_city_id_04cd5a1a_fk_Location_citymaster_id" FOREIGN KEY (city_id) REFERENCES public."Location_citymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_country_id_50088a31_fk_Location_countrymaster_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_country_id_50088a31_fk_Location_countrymaster_id" FOREIGN KEY (country_id) REFERENCES public."Location_countrymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Brands_company Brands_company_state_id_dd39f16b_fk_Location_statemaster_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Brands_company"
    ADD CONSTRAINT "Brands_company_state_id_dd39f16b_fk_Location_statemaster_id" FOREIGN KEY (state_id) REFERENCES public."Location_statemaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Customers_customer_otp Customers_customer_o_customer_id_4a5ab955_fk_Customers; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customer_otp"
    ADD CONSTRAINT "Customers_customer_o_customer_id_4a5ab955_fk_Customers" FOREIGN KEY (customer_id) REFERENCES public."Customers_customerprofile"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Customers_customerprofile Customers_customerpr_company_id_e735d378_fk_Brands_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customerprofile"
    ADD CONSTRAINT "Customers_customerpr_company_id_e735d378_fk_Brands_co" FOREIGN KEY (company_id) REFERENCES public."Brands_company"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Customers_customerprofile Customers_customerprofile_auth_user_id_3fdfc02d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Customers_customerprofile"
    ADD CONSTRAINT "Customers_customerprofile_auth_user_id_3fdfc02d_fk_auth_user_id" FOREIGN KEY (auth_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Location_areamaster Location_areamaster_city_id_6a460ea6_fk_Location_citymaster_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_areamaster"
    ADD CONSTRAINT "Location_areamaster_city_id_6a460ea6_fk_Location_citymaster_id" FOREIGN KEY (city_id) REFERENCES public."Location_citymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Location_citymaster Location_citymaster_state_id_6ab4cb92_fk_Location_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_citymaster"
    ADD CONSTRAINT "Location_citymaster_state_id_6ab4cb92_fk_Location_" FOREIGN KEY (state_id) REFERENCES public."Location_statemaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Location_countrymaster Location_countrymast_currency_id_91e69f4c_fk_Configura; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_countrymaster"
    ADD CONSTRAINT "Location_countrymast_currency_id_91e69f4c_fk_Configura" FOREIGN KEY (currency_id) REFERENCES public."Configuration_currencymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: Location_statemaster Location_statemaster_country_id_0ba51b0a_fk_Location_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Location_statemaster"
    ADD CONSTRAINT "Location_statemaster_country_id_0ba51b0a_fk_Location_" FOREIGN KEY (country_id) REFERENCES public."Location_countrymaster"(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rest_framework_tracking_apirequestlog rest_framework_track_user_id_671b70b7_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rest_framework_tracking_apirequestlog
    ADD CONSTRAINT rest_framework_track_user_id_671b70b7_fk_auth_user FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

