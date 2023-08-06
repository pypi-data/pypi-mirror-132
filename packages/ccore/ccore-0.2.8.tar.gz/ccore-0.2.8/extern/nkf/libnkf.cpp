/*
Changes.
2021.12.06  add cmake compile. libnkf for c++ function.
            * nkf_convert
            * nkf_guess
                 by kirin123kirin library for C++ Custom
2009.6.2    Remove WISH_TRUE, use get_guessed_code() for nkf-2.0.9
                 by SATOH Fumiyasu (fumiyas @ osstech co jp)
2008.7.17   Change the type of strlen from long to int, by SATOH Fumiyasu.
2007.2.1    Add guess() function.
2007.1.13   Remove nkf_parseopts(), by SATOH Fumiyasu.
*/
/**  Python Interface to NKF
***************************************************************************
**  Copyright (c) 2005 Matsumoto, Tadashi <ma2@city.plala.jp>
**  All Rights Reserved.
**
**    Everyone is permitted to do anything on this program
**    including copying, modifying, improving,
**    as long as you don't try to pretend that you wrote it.
**    i.e., the above copyright notice has to appear in all copies.
**    Binary distribution requires original version messages.
**    You don't have to ask before copying, redistribution or publishing.
**    THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE.
***************************************************************************/
#include "libnkf.h"
#include <setjmp.h>
#include <stdio.h>

#undef getc
#undef ungetc
#define getc(f) nkf_getc(f)
#define ungetc(c, f) nkf_ungetc(c, f)

#undef putchar
#undef TRUE
#undef FALSE
#define putchar(c) nkf_putchar(c)

static int nkf_ibufsize, nkf_obufsize;
static unsigned char *nkf_inbuf, *nkf_outbuf;
static int nkf_icount, nkf_ocount;
static unsigned char *nkf_iptr, *nkf_optr;
static jmp_buf env;
static int nkf_guess_flag;

static int nkf_getc(FILE* f) {
    unsigned char c;
    if(nkf_icount >= nkf_ibufsize)
        return EOF;
    c = *nkf_iptr++;
    nkf_icount++;
    return (int)c;
}

static int nkf_ungetc(int c, FILE* f) {
    if(nkf_icount--) {
        *(--nkf_iptr) = c;
        return c;
    } else {
        return EOF;
    }
}

static void nkf_putchar(int c) {
    size_t size;
    unsigned char* p;

    if(nkf_guess_flag) {
        return;
    }

    if(nkf_ocount--) {
        *nkf_optr++ = c;
    } else {
        size = nkf_obufsize + nkf_obufsize;
        p = (unsigned char*)realloc(nkf_outbuf, size + 1);
        if(nkf_outbuf == NULL) {
            longjmp(env, 1);
        }
        nkf_outbuf = p;
        nkf_optr = nkf_outbuf + nkf_obufsize;
        nkf_ocount = nkf_obufsize;
        nkf_obufsize = size;
        *nkf_optr++ = c;
        nkf_ocount--;
    }
}

#define PERL_XS 1
#include "nkf.c"
#include "utf8tbl.c"

/* 
  opts : below reference
    https://github.com/kirin123kirin/nkf#options
 */
extern std::string nkf_convert(std::string& str, std::string& opts) {
    nkf_ibufsize = str.size() + 1;
    nkf_obufsize = nkf_ibufsize * 1.5 + 256;
    nkf_outbuf = (unsigned char*)malloc(nkf_obufsize);
    if(nkf_outbuf == NULL) {
        return NULL;
    }
    nkf_outbuf[0] = '\0';
    nkf_ocount = nkf_obufsize;
    nkf_optr = nkf_outbuf;
    nkf_icount = 0;
    nkf_inbuf = (unsigned char*)str.data();
    nkf_iptr = nkf_inbuf;
    nkf_guess_flag = 0;

    if(setjmp(env) == 0) {
        reinit();

        options((unsigned char*)opts.data());

        kanji_convert(NULL);

    } else {
        free(nkf_outbuf);
        return NULL;
    }

    *nkf_optr = 0;
    std::string res((const char*)nkf_outbuf);
    free(nkf_outbuf);
    return res;
}
extern std::string nkf_convert(unsigned char* str, int strlen, unsigned char* opts) {
    nkf_ibufsize = strlen + 1;
    nkf_obufsize = nkf_ibufsize * 1.5 + 256;
    nkf_outbuf = (unsigned char*)malloc(nkf_obufsize);
    if(nkf_outbuf == NULL) {
        return NULL;
    }
    nkf_outbuf[0] = '\0';
    nkf_ocount = nkf_obufsize;
    nkf_optr = nkf_outbuf;
    nkf_icount = 0;
    nkf_inbuf = nkf_iptr = str;
    nkf_guess_flag = 0;

    if(setjmp(env) == 0) {
        reinit();

        options(opts);

        kanji_convert(NULL);

    } else {
        free(nkf_outbuf);
        return NULL;
    }

    *nkf_optr = 0;
    std::string res((const char*)nkf_outbuf);
    free(nkf_outbuf);
    return res;
}

extern const char* nkf_guess(std::string& str) {
    const char* codename;

    nkf_ibufsize = str.size() + 1;
    nkf_icount = 0;
    nkf_inbuf = (unsigned char*)str.data();
    nkf_iptr = nkf_inbuf;

    nkf_guess_flag = 1;
    reinit();
    guess_f = 1;

    kanji_convert(NULL);

    codename = get_guessed_code();

    return get_guessed_code();
}

extern const char* guess_encoding(const std::string& str) {
    nkf_ibufsize = str.size() + 1;
    nkf_icount = 0;
    nkf_inbuf = (unsigned char*)str.data();
    nkf_iptr = nkf_inbuf;

    nkf_guess_flag = 1;
    reinit();
    guess_f = 1;

    kanji_convert(NULL);

    struct input_code* p = find_inputcode_byfunc(iconv);

    if(input_codename && !*input_codename) {
        return NULL;
    } else if(!input_codename) {
        return "ascii";
    } else if(strcmp(input_codename, "Shift_JIS") == 0) {
        return "cp932";
    } else if(strcmp(input_codename, "EUC-JP") == 0) {
        if(p->score & SCORE_X0213)
            return "euc_jis_2004";  // EUC-JIS-2004
        else if(p->score & (SCORE_X0212))
            return "euc_jp";  // EUCJP-MS
        else if(p->score & (SCORE_DEPEND | SCORE_CP932))
            return "euc_jp";  // CP51932
        return "euc_jp";      // CP51932
    } else if(strcmp(input_codename, "ISO-2022-JP") == 0) {
        if(p->score & (SCORE_KANA))
            return "iso2022_jp_1";  // CP50221
        else if(p->score & (SCORE_DEPEND | SCORE_CP932))
            return "iso2022_jp";  // CP50220
        return "iso2022_jp";      // CP50220
    }
    return input_codename;
}

extern const char* guess_encoding(unsigned char* str, int strlen) {
    nkf_ibufsize = strlen + 1;
    nkf_icount = 0;
    nkf_inbuf = nkf_iptr = str;

    nkf_guess_flag = 1;
    reinit();
    guess_f = 1;

    kanji_convert(NULL);

    struct input_code* p = find_inputcode_byfunc(iconv);

    if(input_codename && !*input_codename) {
        return NULL;
    } else if(!input_codename) {
        return "ascii";
    } else if(strcmp(input_codename, "Shift_JIS") == 0) {
        return "cp932";
    } else if(strcmp(input_codename, "EUC-JP") == 0) {
        if(p->score & SCORE_X0213)
            return "euc_jis_2004";  // EUC-JIS-2004
        else if(p->score & (SCORE_X0212))
            return "euc_jp";  // EUCJP-MS
        else if(p->score & (SCORE_DEPEND | SCORE_CP932))
            return "euc_jp";  // CP51932
        return "euc_jp";      // CP51932
    } else if(strcmp(input_codename, "ISO-2022-JP") == 0) {
        if(p->score & (SCORE_KANA))
            return "iso2022_jp_1";  // CP50221
        else if(p->score & (SCORE_DEPEND | SCORE_CP932))
            return "iso2022_jp";  // CP50220
        return "iso2022_jp";      // CP50220
    }
    return input_codename;
}

