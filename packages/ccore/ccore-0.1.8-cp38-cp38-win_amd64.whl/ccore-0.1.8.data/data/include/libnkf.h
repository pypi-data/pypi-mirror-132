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
#ifndef LIBNKF_H
#define LIBNKF_H

#include <string>

extern std::string nkf_convert(std::string& str, std::string& opts);

extern std::string nkf_convert(unsigned char* str, int strlen, unsigned char* opts);

extern const char* nkf_guess(std::string& str);

extern const char* guess_encoding(const std::string& str);

extern const char* guess_encoding(unsigned char* str, int strlen);

#endif /* LIBNKF_H */
