// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_ELLIPSOID_PROPOSAL_H
#define SAMPLY_ELLIPSOID_PROPOSAL_H

#include <Eigen/Dense>

#include "commons.h"
#include "helpers/sampling_helper.h"
#include "rays_packet.h"
#include "reparametrized_object.h"

namespace samply {

/**
 * @brief Proposes directions sampled from an n-dimensional ellipsoid.
 *
 * @tparam Scalar Type used to describe the directions.
 */
template <typename ScalarType>
class EllipsoidProposal {
public:
    /**
     * @brief Type used to describe the directions.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Type of rays packets constructed from this proposal.
     */
    typedef RaysPacket<ScalarType> RaysPacketType;

    EllipsoidProposal(const AffineTransform<Scalar>& proposal_transform)
        : proposal_transform_(proposal_transform),
          dimensionality_(proposal_transform.get_linear().cols())
    {
    }

    Matrix<Scalar> get_directions(const Eigen::Index num_directions);

    /**
     * @brief Get the dimensionality of the proposal distribution.
     *
     * @return The dimensionality of the proposal distribution.
     */
    Eigen::Index dimensionality() const
    {
        return dimensionality_;
    }

    ReparametrizedObject<EllipsoidProposal<Scalar>>
    get_optimally_reparametrized_descriptor() const;

private:
    const AffineTransform<Scalar> proposal_transform_;
    const Eigen::Index dimensionality_;

    // Helper object used to generate random numbers.
    SamplingHelper sampling_helper_;
};

//==============================================================================
//	EllipsoidProposal public methods implementation.
//==============================================================================

template <typename ScalarType>
Matrix<ScalarType> EllipsoidProposal<ScalarType>::get_directions(
    const Eigen::Index num_directions)
{
    return proposal_transform_ *
           sampling_helper_.get_random_directions<Scalar>(
               static_cast<int>(dimensionality()), static_cast<int>(num_directions));
}

template <typename ScalarType>
ReparametrizedObject<EllipsoidProposal<ScalarType>>
EllipsoidProposal<ScalarType>::get_optimally_reparametrized_descriptor() const
{
    return ReparametrizedObject<EllipsoidProposal<Scalar>>(
        EllipsoidProposal<Scalar>(AffineTransform<double>::identity(dimensionality())),
        proposal_transform_, proposal_transform_.inverse());
}

}  // namespace samply

#endif